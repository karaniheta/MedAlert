from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .models import CustomUser, HealthTip, FirstAidCondition
from .serializers import (
    UserSerializer, UpdateUserSerializer, RegisterSerializer,
    HealthTipSerializer, FirstAidConditionSerializer,
    AppointmentSerializer, AmbulanceSerializer
)
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.contrib.auth import logout
from django.core.management import call_command
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import HealthTip
from django.shortcuts import render, redirect 
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import authenticate, login 
import json
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
                'msg': 'Login successful'
            }, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials or inactive account'}, status=status.HTTP_401_UNAUTHORIZED)

class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        serializer = UpdateUserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Profile updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh_token')
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()  # Blacklist the refresh token (if using a blacklist approach)
            return Response({"message": "Successfully logged out!"}, status=200)
        except Exception as e:
            return Response({"error": "Failed to logout properly."}, status=400)

class HealthTipView(APIView):
    def get(self, request):
        tips = HealthTip.objects.all().order_by('-created_at')
        serializer = HealthTipSerializer(tips, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data

        # Check if data is a list
        if isinstance(data, list):
            serializer = HealthTipSerializer(data=data, many=True)
        else:
            serializer = HealthTipSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FirstAidConditionView(APIView):
    def get(self, request):
        conditions = FirstAidCondition.objects.prefetch_related('sections').all().order_by('-created_at')
        serializer = FirstAidConditionSerializer(conditions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        is_many = isinstance(request.data, list)
        serializer = FirstAidConditionSerializer(data=request.data, many=is_many)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'First aid condition(s) created successfully'}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookAppointmentView(APIView):
    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Appointment booked successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookAmbulanceView(APIView):
    def post(self, request):
        serializer = AmbulanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Ambulance requested successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RunMigrationView(APIView):
    def get(self, request):
        try:
            call_command('makemigrations')
            call_command('migrate')
            return Response({"message": "Migrations applied successfully."})
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        
@csrf_protect
def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
        else:
            User = get_user_model()
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists.')
            else:
                user = User.objects.create_user(email=email, password=password)
                login(request, user)  # Automatically log in the user after registration
                messages.success(request, 'Account created successfully.')
                return redirect('home')  # Redirect to the home page after successful registration

    return render(request, 'register.html')


@login_required
def profile_view(request):
    # Fetch the logged-in user's details
    user = request.user

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')  # Redirect back to the profile page after successful update
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ProfileForm(instance=user)

    return render(request, 'profile.html', {'form': form, 'user': user})

@csrf_protect
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)  # Login the user
            messages.success(request, 'Login successful.')
            return redirect('home')  # Redirect to the home page or wherever you want
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'login.html')

def first_aid_conditions_view(request):
    conditions = FirstAidCondition.objects.prefetch_related('sections').all().order_by('-created_at')
    return render(request, 'first_aid_conditions.html', {'conditions': conditions})

def home(request):
    health_tips = HealthTip.objects.all() 
    return render(request, 'home.html',{'health_tips': health_tips})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')  # Redirect to the login page after logout

# @login_required
# def profile_view(request):
#     # Fetch the logged-in user's details
#     user = request.user

#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES, instance=user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Profile updated successfully!')
#             return redirect('profile')  # Redirect back to the profile page after successful update
#         else:
#             messages.error(request, 'Please correct the errors below.')
#     else:
#         form = ProfileForm(instance=user)

#     return render(request, 'profile.html', {'form': form, 'user': user})
