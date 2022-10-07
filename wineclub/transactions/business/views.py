from urllib import request
from rest_framework import generics
from .serializers import TransactionSerializer
from ..models import Transaction
from rest_framework import permissions
from rest_framework_simplejwt import authentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.db.models import Q

class ListTransactionAPI(generics.ListAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTAuthentication]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['sender','receiver']
    filterset_fields = ['type','sender','receiver', 'currency']
    ordering_fields = ['created','amount','net','fee']

    def get_queryset(self):
        return Transaction.objects.filter(
            Q(sender=self.request.user.email) | 
            Q(receiver=self.request.user.email))
