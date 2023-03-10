from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
# Create your views here.
from .models import *
from .serializers import CoinsSerializer


def getCoin(user):
    queryset = Coins.objects.filter(user=user)
    print(queryset.values())
    # data = CoinsSerializer(queryset).data
    data = queryset.values()
    return list(data)
