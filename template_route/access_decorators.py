from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status

def un_authenticated_user(Wrapped):
    def wrapper(request,*args, **kwargs):
    
        print(f'request:{request.user}')
        if (not request.user.is_authenticated) and request.user == "AnonymousUser":
            return Wrapped(request,*args, **kwargs)
        else:
            resps = '''
                <h1>UnAuthorized  !</h1>                
                <script type="text/javascript">
                    window.location = "/";
                </script>
            '''
            # return HttpResponse(resps, status=status.HTTP_401_UNAUTHORIZED)
            return render(request,'unAuthorized.html')
    return wrapper