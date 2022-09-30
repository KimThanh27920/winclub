#App imports
from bases.administrator.views import BaseAdminViewset
from accounts.models import Account
from wineries.models import Winery
from wines.models import Wine
from coupons.models import Coupon
from reviews.models import Review
from .serializers import CustomerSerializer, BlockCustomerSerializer, BusinessRetrieveSerializer, BusinessSerializer, BlockBusinessSerializer
from bases.errors.errors import BusinessErrors, AccountErrors
# rest_fremawork imports
from rest_framework.response import Response
#django import
from django.utils import timezone


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
        return Account.objects.filter(is_business = False).filter(is_superuser = False).order_by("-updated_at")

    def perform_create(self, serializer):
        pass
    
    def update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        instance = self.get_object()
        error = AccountErrors.exists(instance.id)
        if error is not None:
            return error
        acc = Account.objects.get(id=instance.id)
    
        if acc.is_active == True:
            data = {
                "is_active": False
            }
            Review.objects.filter(created_by=instance.id).update(deleted_at=timezone.now(), deleted_by = self.request.user)
        else:
            data = {
                "is_active": True
            }
            Review.objects.filter(created_by=instance.id).update(deleted_at=None, deleted_by = None)
            
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
        return Winery.objects.exclude(deleted_at__isnull=False).order_by('-updated_at').select_related('account')

    def perform_create(self, serializer):
        pass
    
    def update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        instance = self.get_object()
        error = BusinessErrors.exists(instance.id)
     
        if error is not None:
            return error
        winery = Winery.objects.filter(id=instance.id).first()
    
        acc = Account.objects.get(id=winery.account_id)
        print(acc.id)
        if winery.is_active == True:
            data = {
                "is_active": False
            }
            acc.is_business= False
            acc.save()
            
            # block wine of winery
            wines = Wine.objects.filter(winery=instance.id)
            for wine in wines:
                if wine.is_active == True:
                    wine.is_active = False
                    wine.updated_by = self.request.user
                    wine.updated_at=timezone.now()
                    wine.save( )
           
            #block coupon of winery
            coupons = Coupon.objects.filter(created_by=instance.id)
            for coupon in coupons:
                if coupon.is_active == True:
                    coupon.is_active = False
                    coupon.updated_by = self.request.user
                    coupon.updated_at=timezone.now()
                    coupons.save( )
        else:
            data = {
                "is_active": True
            }
            acc.is_business= True
            acc.save()

            # active wine of winery
            wines = Wine.objects.filter(winery=instance.id)
            for wine in wines:
                if wine.is_active == False and wine.updated_by.id == acc.id :
                   pass
                else:
                    wine.is_active = True
                    wine.updated_by = self.request.user
                    wine.updated_at=timezone.now()
                    wine.save()
                   
            #active coupon of winery
            coupons = Coupon.objects.filter(created_by=instance.id)
            for coupon in coupons:
                if coupon.is_active == False and coupon.updated_by.id == acc.id :
                   pass
                else:
                    coupon.is_active = True
                    coupon.updated_by = self.request.user
                    coupon.updated_at=timezone.now()
                    coupon.save()

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

