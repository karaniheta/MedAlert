# user/serializers.py

from rest_framework import serializers
from .models import CustomUser  
from .utils import send_signup_email

class UserSerializer(serializers.ModelSerializer):
    profile_picture_url = serializers.SerializerMethodField()
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'age', 'gender','profile_picture_url']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        
        user = CustomUser.objects.create_user(**validated_data)
        return user
    def get_profile_picture_url(self, obj):
        return obj.profile_picture.url if obj.profile_picture else None

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        email = validated_data.get('email')
        username = email.split('@')[0]  
        user = CustomUser.objects.create_user(**validated_data)
        send_signup_email(email, username)
        return user

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'age', 'gender', 'profile_picture', 'profile_picture_url']
        
    def update(self, instance, validated_data):
        if 'profile_picture' in validated_data:
            profile_picture = validated_data.pop('profile_picture')
            instance.profile_picture = profile_picture
        return super().update(instance, validated_data)
