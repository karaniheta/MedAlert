from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from cloudinary.models import CloudinaryField
import cloudinary.uploader

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, username=None, **extra_fields):
        """
        Create and return a regular user with an email and password.
        """
        if not email:
            raise ValueError("Email is required")
        
        email = self.normalize_email(email)
        
        if not username:
            username = email.split('@')[0]
        
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)  
        user.save(using=self._db)  
        return user

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    profile_picture = CloudinaryField('image', null=True, blank=True)
    profile_picture_url = models.URLField(null=True, blank=True)  


   
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'age', 'gender']

    objects = CustomUserManager()  

    def save(self, *args, **kwargs):
        if self.profile_picture:
            upload_result = cloudinary.uploader.upload(self.profile_picture)
            self.profile_picture_url = upload_result['secure_url']  
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

class HealthTip(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    category = models.CharField(max_length=100, blank=True)
    source = models.CharField(max_length=255, blank=True, null=True)  
    importance_level = models.IntegerField(default=1)  
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_healthtip'  
    def __str__(self):
        return self.title


class FirstAidCondition(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=50, default='General')
    urgency_level = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_firstaidcondition' 

    def __str__(self):
        return self.title

class FirstAidSection(models.Model):
    condition = models.ForeignKey(FirstAidCondition, related_name='sections', on_delete=models.CASCADE)
    heading = models.CharField(max_length=255)
    content = models.TextField()
    step_number = models.IntegerField(default=1)  

    def __str__(self):
        return f"{self.condition.title} - {self.heading}"

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    specialist = models.CharField(max_length=100)
    hospital= models.CharField(max_length=100, default='Cooper Hospital')

class AmbulanceBooking(models.Model):
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)
    address = models.TextField()