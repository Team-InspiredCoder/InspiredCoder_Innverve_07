from django.urls import path
from accounts.views import *

urlpatterns = [
    path('register', Register.as_view(), name="register"),
    path('login', Login.as_view(), name="login"),
    path('verify-user/<str:vmode>', VerifyUser.as_view(), name="verify-user"),
    path('resend-otp', ResendOTP.as_view(), name="resend-otp"),

    # test
    path('link/verify/<str:token>', verifyLink, name="verify-link"),

]

