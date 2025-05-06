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
from django.contrib.auth import logout
from django.core.management import call_command
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            return Response({
                'access_token': access_token,
                'refresh_token': refresh_token,
                'msg': 'User created and logged in successfully'
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
        # This will only log out the user by revoking the refresh token, ensuring no new access token can be issued.
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
