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
from user.views import register_view,login_view,profile_view,first_aid_conditions_view,book_ambulance_view,logout_view,home,first_aid_conditions_view,book_appointment_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),

    path('first_aid_conditions/', first_aid_conditions_view, name='first_aid_conditions_view'),
    path('profile/', profile_view, name='profile'), 
    path('register/', register_view, name='register'),
    path('ambulance/', book_ambulance_view, name='ambulance'),
    path('admin/', admin.site.urls),
    path('logout/',logout_view, name='logout'),
    path('appointment/',book_appointment_view, name='appointment'),
    path('first-aid-conditions/', first_aid_conditions_view, name='first_aid_conditions'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
