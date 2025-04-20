from django.core.mail import send_mail
from django.conf import settings
import os
from dotenv import load_dotenv
load_dotenv()

def send_signup_email(to_email, username):
    subject = 'Welcome to MedAlert!'
    text_content = f'Hi {username},\n\nThanks for signing up. We’re glad to have you onboard! ' 

    msg = send_mail(subject, text_content,os.getenv('EMAIL_HOST_USER'), [to_email],fail_silently=False)
