"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user.views import RegisterView, LoginView,LogoutView,UpdateProfileView, HealthTipList, FirstAidConditionList,BookAmbulanceView,BookAppointmentView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('update/', UpdateProfileView.as_view(),name='update'),
    path('api/health-tips/', HealthTipList.as_view(), name='healthtip-list'),
    path('api/first-aid-conditions/', FirstAidConditionList.as_view(), name='firstaidcondition-list'),
    path('appointment/', BookAppointmentView.as_view(), name='appointment'),
    path('ambulance/', BookAmbulanceView.as_view(), name='ambulance'),
    # path('success/', views.success, name='success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
