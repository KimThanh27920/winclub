import logging
from django.conf import settings
from wineclub.celery import app
from bases.services.firebase.notification import send_notify_message

@app.task()
def send_background_notification(user_id, msg_title, msg_body):
    send_notify_message(user_id, msg_title, msg_body) 
    return "Done send notification"