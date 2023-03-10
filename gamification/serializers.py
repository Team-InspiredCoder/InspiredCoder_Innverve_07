from rest_framework import serializers

# from .views import *
from .models import *

# CustomUser model serializer
class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = '__all__'
        
class CoinsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coins
        fields = '__all__'





