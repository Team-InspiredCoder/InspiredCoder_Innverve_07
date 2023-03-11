from django.urls import path
from accounts.views import *
from interview.views import *
from template_route.views import *


urlpatterns = [
    path('', index, name="index"),
    path('register', register, name="register"),
    path('login', login, name="login"),
    path('verify-email/<str:action>/<str:email>/<str:name>', verifyEmail, name="verify-email"),
    path('email-verified', emailVerified, name="email-verified"),

    path('interview-preview', interviewPreview, name="interview-preview"),
    path('interview-screen', interviewScreen, name="interview-screen"),
    path('generate-pdf', generate_pdf, name="generate-pdf"),
]

