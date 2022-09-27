from fcm_django.models import FCMDevice
from firebase_admin.messaging import Message, Notification


def send_notify_message(device, msg_title, msg_body):
    message = Message(
        notification=Notification(
            title="Test notification", body="Test single notification"
        )
    )
    device.send_message(message)


def get_device_user(user_id):
    device = FCMDevice.objects.filter(user=user_id, active=True)
    return device
