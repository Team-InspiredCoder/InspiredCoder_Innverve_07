from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse

# from .serializers import BadgeSerializer
# Create your views here.
from .models import *

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import *
# from gamification.serializers import BadgeSerializer
class BadgeView(APIView):
   permission_classes = [IsAuthenticated]
   authentication_classes = [JWTAuthentication] 
   def get(self,request):
      queryset = Badge.objects.filter(user=request.user)  
      # data = BadgeSerializer(queryset,many=True).data

      return JsonResponse({"data":list(queryset.values())})
   
def createbadge(request):
    data = request.data
    badge_serializers = BadgeSerializer(data=data)
    data['user'] = request.user
    if badge_serializers.is_valid():
            badge_serializers.save()
    else:
        return JsonResponse({"error":badge_serializers.errors})  
          
#this function will be called on the  termination of an interview
def updatebadge(request):
    badge_queryset = Badge.objects.filter(user=request.user)
    confidence = request.data.get('confidence')
    answer_accuracy = request.data.get('answer_accuracy')
    
    confidence_batch = badge_queryset.filter(b_type='confidence').last()
    answer_batch = badge_queryset.filter(b_type='answer').last()
    normal_batch = badge_queryset.filter(b_type='normal').last()

    confidence_progress = confidence_batch.progress
    answer_progress = answer_batch.progress
    normal_progress = normal_batch.progress
    
    confidence_level = confidence_batch.level
    answer_level = answer_batch.level
    normal_level = normal_batch.level



    if confidence>80:
        confidence_progress = confidence_progress + 1
    if answer_accuracy>85:
        answer_progress = answer_progress + 1
    if normal_progress>85:
        normal_progress = normal_progress + 1

    if confidence_progress >=15:
       confidence_level  = "gold"
    elif confidence_progress>=10:
       confidence_level  = "silver"
    
    elif confidence_progress>=5:
       confidence_level  = "bronze"
        

    if answer_progress >=15:
       answer_level  = "gold"
    elif answer_progress>=10:
       answer_level  = "silver"
    
    elif answer_progress>=5:
       answer_level  = "bronze"
    
    

    badge_queryset.filter(b_type='confidence').update(level=confidence_level,progress=confidence_progress)
    badge_queryset.filter(b_type='answer').update(level=answer_level,progress=answer_progress)

    ## Response Need to be Send ..
             
