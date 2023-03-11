from django.urls import path
from .views import *

urlpatterns = [
    path('generate-pdf',GeneratePdf.as_view()),
]