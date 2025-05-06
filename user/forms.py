# from django import forms
# from .models import Appointment, AmbulanceBooking

# class AppointmentForm(forms.ModelForm):
#     class Meta:
#         model = Appointment
#         fields = '__all__'

# class AmbulanceForm(forms.ModelForm):
#     class Meta:
#         model = AmbulanceBooking
#         fields = '__all__'

# forms.py

from django import forms
from .models import CustomUser

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'age', 'gender', 'profile_picture']  # Include the fields you want to edit

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        # Add any additional customization for the form if needed
