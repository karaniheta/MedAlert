
from django import forms
from .models import CustomUser,Appointment,AmbulanceBooking

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'age', 'gender', 'profile_picture'] 

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'phone_no', 'age', 'gender', 'specialist', 'hospital']
        widgets = {
            'gender': forms.Select(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
        }

class AmbulanceBookingForm(forms.ModelForm):
    class Meta:
        model = AmbulanceBooking
        fields = ['name', 'phone_no', 'address']