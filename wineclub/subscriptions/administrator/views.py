#App imports
from bases.administrator.views import BaseAdminViewset
from .serializers import SubscriptionPackageReadSerializer, SubscriptionPackageSerializer
from subscriptions.models import SubscriptionPackage
from service.stripe.stripe_api import StripeAPI

#Type Admin Viewset
class SubscriptionsPackageAdminAPIView(BaseAdminViewset):

    serializer_class = {
        "list": SubscriptionPackageReadSerializer,
        "retrieve": SubscriptionPackageReadSerializer,
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
       
        price_id = StripeAPI.create_price(
            name = data["name"],
            price=price,
            currency=data["currency"],
            interval=data["interval"],
            interval_count=data["interval_count"])

        serializer.save(price_id=price_id,
                     updated_by=self.request.user,
                        created_by=self.request.user)