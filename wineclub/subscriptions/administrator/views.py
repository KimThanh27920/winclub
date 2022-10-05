#App imports
from bases.administrator.views import BaseAdminViewset
from .serializers import SubscriptionPackageReadSerializer, SubscriptionPackageSerializer, SubscriptionPackageRetrieveSerializer
from subscriptions.models import SubscriptionPackage
from bases.services.stripe.stripe import StripeAPI

#Type Admin Viewset
class SubscriptionsPackageAdminAPIView(BaseAdminViewset):

    serializer_class = {
        "list": SubscriptionPackageReadSerializer,
        "retrieve": SubscriptionPackageRetrieveSerializer,
        "create": SubscriptionPackageSerializer,
        "update": SubscriptionPackageSerializer,
        "delete": SubscriptionPackageSerializer
    }
    
    queryset = SubscriptionPackage.objects.select_related('created_by','updated_by')
    search_fields = ['name','interval']
    filterset_fields = ['is_active','interval_count']
    ordering_fields = ['name','interval_count','price','created_at','updated_at']

    def perform_create(self, serializer):
        data = self.request.data
        price = int(data["price"]*100)
        
        subpk = serializer.save(
                     updated_by=self.request.user,
                        created_by=self.request.user)
        price_id = StripeAPI.create_price(
            name = data["name"],
            price=price,
            currency=data["currency"],
            interval=data["interval"],
            interval_count=data["interval_count"],
            subpk=subpk.id
            )
            
        serializer.save(price_id=price_id)
    
    def perform_update(self, serializer):
        subs = serializer.save(updated_by=self.request.user)
        StripeAPI.delete_price(sub_id=subs.id)
        price = int(subs.price*100)
        price_id = StripeAPI.create_price(
            name = subs.name,
            price=price,
            currency= subs.currency,
            interval=subs.interval,
            interval_count=subs.interval_count,
            subpk=subs.id
            )
        serializer.save(price_id=price_id)
    
    def perform_destroy(self, instance):
        StripeAPI.delete_price(sub_id=instance.id)
        return super().perform_destroy(instance)
