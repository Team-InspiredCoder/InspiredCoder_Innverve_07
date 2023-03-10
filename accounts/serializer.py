from rest_framework.serializers import ModelSerializer
from accounts.models import *



# CustomUser model serializer
class GetCustomUserSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        exclude = ('password', 'is_active', 'is_staff', 'is_superuser', 'email_verified_at', 'user_permissions', 'groups')




