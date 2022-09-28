# App imports
from bases.administrator.views import BaseAdminViewset
from .serializers import TransactionSerializer
from transactions.models import Transaction


#Transaction Admin Viewset
class TransactionAdminView(BaseAdminViewset):

    serializer_class = {
        "list": TransactionSerializer,
        "retrieve": TransactionSerializer,
        "create": TransactionSerializer,
        "update": TransactionSerializer,
        "delete": TransactionSerializer
    }
    
    queryset = Transaction.objects.select_related('sender','receiver')
    search_fields = ['sender','receiver']
    filterset_fields = ['type','sender','receiver']
    ordering_fields = ['timestamp','amount','net','fee','unit']

    def get_queryset(self):
        return super().get_queryset().order_by('-timestamp')
    
    def perform_update(self, serializer):
        pass
    
    def update(self, request, *args, **kwargs):
        pass

    def destroy(self, request, *args, **kwargs):
        pass