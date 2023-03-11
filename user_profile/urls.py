from django.urls import path
from .views import *

urlpatterns = [
 path('experience-crud',UserExperienceCRUD.as_view()),
]