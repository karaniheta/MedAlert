# user/serializers.py

from rest_framework import serializers
from .models import CustomUser, HealthTip, FirstAidCondition, FirstAidSection,Appointment,AmbulanceBooking
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
        fields = ['email','username', 'age', 'gender', 'profile_picture', 'profile_picture_url']
        
    def update(self, instance, validated_data):
        if 'profile_picture' in validated_data:
            profile_picture = validated_data.pop('profile_picture')
            instance.profile_picture = profile_picture
        return super().update(instance, validated_data)
class HealthTipSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthTip
        fields = ['id', 'title', 'summary', 'category', 'source', 'importance_level', 'created_at']

class FirstAidSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstAidSection
        fields = ['id', 'heading', 'content', 'step_number']

class FirstAidConditionSerializer(serializers.ModelSerializer):
    sections = FirstAidSectionSerializer(many=True)

    class Meta:
        model = FirstAidCondition
        fields = ['id', 'title', 'description', 'category', 'urgency_level', 'created_at', 'sections']

    def create(self, validated_data):
        sections_data = validated_data.pop('sections')
        condition = FirstAidCondition.objects.create(**validated_data)
        for section in sections_data:
            FirstAidSection.objects.create(condition=condition, **section)
        return condition


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class AmbulanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmbulanceBooking
        fields = '__all__'