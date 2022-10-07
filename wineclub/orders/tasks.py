import logging
from django.conf import settings
from wineclub.celery import app
from bases.services.firebase.notification import send_notify_message
from django.core.mail import send_mail


@app.task()
def send_background_notification(user_id, msg_title, msg_body):
    send_notify_message(user_id, msg_title, msg_body)
    return "Done send notification"


@app.task()
def send_background_email_notify(title_mail, message, receiver):
    send_mail(
            subject=title_mail,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[receiver],
        )
    return "Done send mail notify"
