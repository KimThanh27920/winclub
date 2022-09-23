#App imports
from bases.administrator.views import BaseAdminViewset
from .serializers import SubscriptionPackageReadSerializer, SubscriptionPackageSerializer
from subscriptions.models import SubscriptionPackage


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

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
 