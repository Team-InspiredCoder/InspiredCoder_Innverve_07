from django.http import HttpResponse
from rest_framework import status
def un_authenticated_user(Wrapped):
    def wrapper(request,*args, **kwargs):

        print(f'request:{request.user}')
        if (not request.user.is_authenticated) and request.user == "AnonymousUser":
            return Wrapped(request,*args, **kwargs)
        else:
            return HttpResponse('Your are not logged in user', status=status.HTTP_401_UNAUTHORIZED)
    return wrapper