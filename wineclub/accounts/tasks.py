
import logging
from django.conf import settings
from django.core.mail import send_mail
from wineclub.celery import app


@app.task()
def send_background_mail(email, html_content):
    send_mail(
            subject='WineClub - Forgot Password',
            message='PIN',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            html_message=html_content
        )
    return "Done send mail " + email
