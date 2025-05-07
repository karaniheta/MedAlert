from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .models import CustomUser, HealthTip, FirstAidCondition
from .forms import ProfileForm,AppointmentForm,AmbulanceBookingForm
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

from django.contrib.auth import authenticate, login 
import json



@csrf_protect
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
        else:
            User = get_user_model()
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                login(request, user)
                messages.success(request, 'Account created successfully.')
                return redirect('home')

    return render(request, 'register.html')

@csrf_protect
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)  # email here

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')
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
    return redirect('login') 

@login_required
def profile_view(request):
    user = request.user

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')  
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ProfileForm(instance=user)

    return render(request, 'profile.html', {'form': form, 'user': user})

@login_required
def book_appointment_view(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()  # Simply save the form if valid
            messages.success(request, 'Appointment booked successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
            print(form.errors) 

    else:
        form = AppointmentForm()

    return render(request, 'appointment.html', {'form': form})


@login_required
def book_ambulance_view(request):
    if request.method == 'POST':
        form = AmbulanceBookingForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Ambulance booked successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Error occured')
            print(form.errors) 

    else:
        form = AmbulanceBookingForm()

    return render(request, 'ambulance.html', {'form': form})