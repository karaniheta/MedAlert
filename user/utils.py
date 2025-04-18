from django.core.mail import EmailMultiAlternatives

def send_signup_email(to_email, username):
    subject = '🎉 Welcome to MedAlert!'
    text_content = f'Hi {username},\n\nThanks for signing up. We’re glad to have you onboard! 🚀'
    html_content = f'<p>Hi {username},</p><p>Thanks for signing up. We’re glad to have you onboard! 🚀</p>'
    
    msg = EmailMultiAlternatives(subject, text_content, settings.DEFAULT_FROM_EMAIL, [to_email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

