from django.shortcuts import render
from .access_decorators import *
# Create your views here.

@un_authenticated_user
def index(request):

    return render(request, 'home/index.html')

@un_authenticated_user
def register(request):

    return render(request, 'login_register/signup.html')


@un_authenticated_user
def login(request):

    return render(request, 'login_register/login.html')


@un_authenticated_user
def verifyEmail(request, action, email, name):
    
    data = {
        "action": action,
        "email": email,
        "name": name
    }

    print("\ndata :: ", data)

    return render(request, 'user_verification/otp.html', data)


@un_authenticated_user
def emailVerified(request):

    return render(request, 'user_verification/activate.html')



def interviewPreview(request):

    return render(request, 'interview/preview.html')




