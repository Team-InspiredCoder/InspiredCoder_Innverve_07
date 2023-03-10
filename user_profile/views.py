from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from user_profile.models import Experience
from .serializers import *
from django.http import JsonResponse
# Create your views here.

# Crud for Experience 

class UserExperienceCRUD(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication] 
    def post(self,request):
        data = request.data 
        data['user'] = request.user.id
        experience_queryset = Experience.objects.filter(company_name=request.data.get('company_name'),
                                                        position=request.data.get('position'),
                                                        )
        print("experience_queryset:",experience_queryset)
        if len(experience_queryset)<=0:
            experience_serializer = ExperienceSerializers(data=data)
            if experience_serializer.is_valid():
                experience_serializer.save()
                return JsonResponse({"msg":"New Record Added Successfully!"})

            else:
                return JsonResponse({"error":experience_serializer.errors})
        
        else:
            return JsonResponse({"message":"Record Already Exists"})
        

    def get(self,request):
        experience = Experience.objects.filter(user=request.user)
        data = ExperienceSerializers(experience,many=True).data
        return JsonResponse({"data":data})
    
    def put(self,request):
        data = request.data
        experience_queryset = Experience.objects.filter(company_name=request.data.get('company_name'),
                                  position=request.data.get('position'))
        if len(experience_queryset)>0:
            experience_serializer =  ExperienceSerializers(instance=experience_queryset.last(),data=request.data)   
            if experience_serializer.is_valid():
                experience_serializer.save()
                return JsonResponse({"msg":"Record Updated Successfully!"})
            else:
                return JsonResponse({"error":experience_serializer.errors})
        
        else:
            return JsonResponse({"msg":"Record Not Found"})
    
    def delete(self,request):
        data = request.data        
        experience_queryset = Experience.objects.filter(company_name=request.data.get('company_name'),
                                  position=request.data.get('position'))
        
        if len(experience_queryset)>0:
            experience_queryset.delete()
            return JsonResponse({"msg":"Particular Record is Deleted"})
        else:
            return JsonResponse({"msg":"Record Not Found"})
    


# class UserEducationCRUD(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication] 
    def post(self,request):
        data = request.data 
        data['user'] = request.user.id
        experience_queryset = Experience.objects.filter(title=request.data.get('title'),
                                                        school_name=request.data.get('school_name'),
                                                        )
        print("experience_queryset:",experience_queryset)
        if len(experience_queryset)<=0:
            experience_serializer = ExperienceSerializers(data=data)
            if experience_serializer.is_valid():
                experience_serializer.save()
                return JsonResponse({"msg":"New Record Added Successfully!"})

            else:
                return JsonResponse({"error":experience_serializer.errors})
        
        else:
            return JsonResponse({"message":"Record Already Exists"})
        

    def get(self,request):
        experience = Experience.objects.filter(user=request.user)
        data = ExperienceSerializers(experience,many=True).data
        return JsonResponse({"data":data})
    
    def put(self,request):
        data = request.data
        experience_queryset = Experience.objects.filter(company_name=request.data.get('company_name'),
                                  position=request.data.get('position'))
        if len(experience_queryset)>0:
            experience_serializer =  ExperienceSerializers(instance=experience_queryset.last(),data=request.data)   
            if experience_serializer.is_valid():
                experience_serializer.save()
                return JsonResponse({"msg":"Record Updated Successfully!"})
            else:
                return JsonResponse({"error":experience_serializer.errors})
        
        else:
            return JsonResponse({"msg":"Record Not Found"})
    
    def delete(self,request):
        data = request.data        
        experience_queryset = Experience.objects.filter(company_name=request.data.get('company_name'),
                                  position=request.data.get('position'))
        
        if len(experience_queryset)>0:
            experience_queryset.delete()
            return JsonResponse({"msg":"Particular Record is Deleted"})
        else:
            return JsonResponse({"msg":"Record Not Found"})

