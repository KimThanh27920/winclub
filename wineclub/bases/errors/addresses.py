# From rest_framework
from rest_framework import status
from rest_framework.response import Response
# From app
from addresses.models import Address
from .bases import return_code_400


def check_address_business_exist(account):
    obj = Address.objects.filter(account=account)
    if(obj.exists()):
        message = "You have created address, You can use, update or remove it for new create"
        return return_code_400(message)
