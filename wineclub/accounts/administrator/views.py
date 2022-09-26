#App imports
from bases.administrator.views import BaseAdminViewset
from accounts.models import Account
from wineries.models import Winery
from .serializers import CustomerSerializer, BlockCustomerSerializer, BusinessRetrieveSerializer, BusinessSerializer, BlockBusinessSerializer
# rest_fremawork imports
from rest_framework.response import Response


#Manage Customer Viewset
class ManageCustomer(BaseAdminViewset):
    
    serializer_class = {
        "list": CustomerSerializer,
        "retrieve": CustomerSerializer,
        "update": CustomerSerializer
    }

    search_fields = ['full_name','email','phone']
    filterset_fields = ['birthday', 'gender', 'is_active']
    ordering_fields = ['email', 'full_name', 'points','birthday', 'last_login']

    def get_queryset(self):
        return Account.objects.filter(is_business = False).filter(is_superuser = False)

    def perform_create(self, serializer):
        pass
    
    def update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        instance = self.get_object()
        acc = Account.objects.get(id=instance.id)
    
        if acc.is_active == True:
            data = {
                "is_active": False
            }
        else:
            data = {
                "is_active": True
            }
        #just update is_active fields
        serializer = BlockCustomerSerializer(instance, data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        serializer = self.get_serializer(instance)
        
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
      

    def perform_destroy(self, instance):
        pass


#Manage Business
class ManageBusiness(BaseAdminViewset):
    
    serializer_class = {
        "list": BusinessSerializer,
        "retrieve": BusinessRetrieveSerializer,
        "update": BusinessSerializer
    }

    search_fields = ['name','phone_winery']
    filterset_fields = ['rating_average', 'reviewer', 'founded_date','is_active']
    ordering_fields = ['name', 'rating_average', 'reviewer', 'founded_date','created_at']

    def get_queryset(self):
        return Winery.objects.exclude(deleted_at__isnull=False).order_by('updated_at').select_related('account')

    def perform_create(self, serializer):
        pass
    
    def update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        instance = self.get_object()
        winery = Winery.objects.get(id=instance.id)
       
        if winery.is_active == True:
            data = {
                "is_active": False
            }
        else:
            data = {
                "is_active": True
            }
        #just update is_active fields
        serializer = BlockBusinessSerializer(instance, data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        serializer = self.get_serializer(instance)
        
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
      

    def perform_destroy(self, instance):
        pass

