from django.urls import path 
from .views import *
urlpatterns = [
    path('get-badge-data',BadgeView.as_view()),
    
]