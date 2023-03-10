from datetime import timedelta, datetime
from django.shortcuts import render
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import auth
from django.db import transaction
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from gamification.models import Coins
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from accounts.models import *
from accounts.serializer import *

import random
import uuid


from gamification.coins import getCoin

# global function here


def sendOTPEmail(email, name, action):

    check_otp, token = createUserVerificationToken(email=email, action=action)
    print(f"\nOTP :: {check_otp} --- token :: {token}")
    domain = "http://127.0.0.1:8000"
    url = f"{domain}api/v1/accounts/link/verify/{token}"

    subject = f"Welcome to Interview.AI {name} !"
    msg = f"OTP :: {check_otp}"
    html_message = render_to_string('mail_template/signup.html', {"check_otp": check_otp, "check_url": url})

    res = send_mail(subject, msg, settings.DEFAULT_FROM_EMAIL, [email, "siddhirajk77gmail.com"], html_message=html_message, fail_silently=False)
    print("res :: ", res)

    if res == 1:
        return True
    else:
        return False




def createUserVerificationToken(email, action):

    UserVerification.objects.filter(email=email, action=action).delete()

    check_otp = random.randint(10000, 99999)
    token = f"{uuid.uuid4()}{uuid.uuid4()}"

    if UserVerification.objects.filter(token=token).exists():
        token = f"{token}{random.randint(100000000, 9999999999)}"

    new_token = UserVerification.objects.create(email=email, otp=check_otp, token=token, action=action, token_expire_on=(
                                                datetime.now() + timedelta(days=1)), otp_expire_on=(datetime.now() + timedelta(minutes=10)))
    new_token.save()

    return check_otp, token




# Create your views here.


def test(request):
    return render(request, 'temp_video.html')


def verifyLink(request, token):
    print("\nToken :: ", token)

    return HttpResponse("Verified !")




class Register(APIView):

    permission_classes = []
    authentication_classes = []

    @transaction.atomic
    def post(self, request):

        rd = request.data
        print("rd :: ", rd)

        if CustomUser.objects.filter(email=rd['email']).exists():
            return Response({"success": False, "error": False, "message": f"User with email '{rd['email']}' already exists !"})

        if not sendOTPEmail(rd['email'], rd['fname'], "signup"):
            return Response({"success":False, "error": False, "message": "Email not sent !"})

        new_user = CustomUser.objects.create_user(email=rd['email'], username=rd['email'], password=rd['password'],
                                                  first_name=rd['fname'], last_name=rd['lname'], mobile_number=rd['phone'],
                                                  gender=rd['gender'], occupation=rd['occupation'], profile_picture=rd['profile_picture'])

        data = {"email": rd['email'], "name": rd['fname'], "action": "signup"}

        return Response({"success": True, "error": False, "message": "Successful !", "data": data})


class Login(APIView):

    permission_classes = []
    authentication_classes = []

    @transaction.atomic
    def post(self, request):

        rd = request.data
        print("rd :: ", rd)

        user = auth.authenticate(email=rd['email'], password=rd['password'])
        print("user:",user)
        if user is not None:

            if not user.is_verified:
                return Response({"success": False, "error": False, "message": "Email is not verified. Please verify Email and try Again !"})

            # pankaj
            coin_data = None
            try:
                coin_queryset = Coins.objects.filter(user=user)
                print(coin_queryset)
                print("len:",len(coin_queryset))
                if len(coin_queryset)<0:
                    new_coin = Coins.objects.create(user=user, value=10, expire_date=datetime.now())
                    new_coin.save()
                    print("In if")
                else:
                    coin_model_obj = coin_queryset.last()
                    updated_coin_val = coin_model_obj.value + 5
                    print('updated_coin_val:',updated_coin_val)
                    coin_model_obj.value = updated_coin_val
                    coin_model_obj.save()
                    # pass

                coin_data = getCoin(user)
                print("coin_data",coin_data)

            except Exception as err:
                print("Error :: ", err)

            token = RefreshToken.for_user(user)
            data = GetCustomUserSerializer(user).data

            return Response({"success": True, "error": False, "message": "User login successfully !", "data": data,
                            "authToken": {
                                'type': 'Bearer',
                                'access': str(token.access_token),
                                'refresh': str(token),
                                'coin_data':coin_data
                            }})
        else:
            return Response({"success": False, "error": False, "message": "Oppps! Creadentials does not matched!"})



class VerifyUser(APIView):

    @transaction.atomic
    def post(self, request, vmode):

        rd = request.data
        print("rd :: ", rd)

        UserVerification.objects.filter(token_expire_on__lte=datetime.now()).delete()
        token_obj = None

        if vmode == "otp":
            token_obj = UserVerification.objects.filter(email=rd['email'], otp=rd['otp'], action=rd['action'], otp_expire_on__gte=datetime.now()).first()
        elif vmode == "token":
            token_obj = UserVerification.objects.filter(token=rd['token'], token_expire_on__gte=datetime.now()).first()
            rd['email'] = token_obj.email
            rd['action'] = token_obj.action

        if token_obj != None and rd['action'] == "signup":

            token_obj.delete()
            user = CustomUser.objects.filter(email=rd['email']).first()
            user.is_verified=True
            user.email_verified_at=datetime.now()
            user.save()

            token = RefreshToken.for_user(user)
            data = GetCustomUserSerializer(user).data

            return Response({"success": True, "error": False, "message": "User Registration successful !", "data": data,
                            "authToken": {
                                'type': 'Bearer',
                                'access': str(token.access_token),
                                'refresh': str(token),
                            }})

        else:
            return Response({"success": False, "error": False, "message": "OTP/Token does not matched!"})

        # return Response({"success": False, "error": False, "message": "Something went wrong !"})


class ResendOTP(APIView):

    permission_classes = []
    authentication_classes = []

    @transaction.atomic
    def post(self, request):

        rd = request.data
        print("rd :: ", rd)

        if not sendOTPEmail(rd['email'], rd['fname'], rd['action']):
            return Response({"success":False, "error": False, "message": "Email not sent !"})
        else:
            return Response({"success":True, "error": False, "message": "Email sent successfully !"})





