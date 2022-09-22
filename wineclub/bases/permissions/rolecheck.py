from urllib import request
from django.contrib.auth import get_user_model

User = get_user_model()


def check_role_business(self, request):
    user = User.objects.get(id = request.user.id)
    return user.is_business