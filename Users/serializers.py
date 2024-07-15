from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueTogetherValidator

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password']
        extra_kwargs = {
           'email': {'required': True},        
        }
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['email',]
                
            )
        ]