#app imports
from bases.guest.views import BaseGuestViewset
from subscriptions.models import SubscriptionPackage
from .serializers import SubscriptionListSerializer, SubscriptionReadOnlySerializer


#Subscription Guest View
class SubscriptionsPackageGuestViews(BaseGuestViewset):
    serializer_class= {
        "list":SubscriptionListSerializer,
        "retrieve":SubscriptionReadOnlySerializer,
        "create": SubscriptionListSerializer,
        "update": SubscriptionListSerializer,
        "delete": SubscriptionListSerializer,
    }

    queryset = SubscriptionPackage.objects.all()
    search_fields = ['name','interval']
    filterset_fields = ['interval_count']
    ordering_fields = ['name','interval_count','price']
