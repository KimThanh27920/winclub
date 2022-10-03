# From rest_framework
from rest_framework import status
from rest_framework.response import Response



def return_code_400(message):
    return Response(data={"message": message}, status=status.HTTP_400_BAD_REQUEST)