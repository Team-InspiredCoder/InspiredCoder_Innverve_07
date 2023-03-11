from rest_framework import serializers
from .models import *


class ExperienceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class EducationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'
class SkillsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'