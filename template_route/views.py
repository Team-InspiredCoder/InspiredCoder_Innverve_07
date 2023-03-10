from django.shortcuts import render

# Create your views here.


def index(request):

    return render(request, 'home/index.html')


def register(request):

    return render(request, 'login_register/signup.html')


def login(request):

    return render(request, 'login_register/login.html')


def verifyEmail(request, action, email, name):
    
    data = {
        "action": action,
        "email": email,
        "name": name
    }

    print("\ndata :: ", data)

    return render(request, 'user_verification/otp.html', data)


def emailVerified(request):

    return render(request, 'user_verification/activate.html')


def interviewPreview(request):

    return render(request, 'interview/preview.html')


def interviewScreen(request):

    return render(request, 'interview/interview_page.html')




