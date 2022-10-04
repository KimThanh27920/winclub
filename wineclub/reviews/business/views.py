from rest_framework_simplejwt import authentication
from rest_framework import generics, permissions

from . import serializers
from reviews.models import Review
from wines.models import Wine
from wineries.models import Winery

from bases.permissions.business import IsBusiness


class ListReviewsAPIView(generics.ListAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsBusiness]
    serializer_class = serializers.ReviewSerializer

    def get_queryset(self):
        winery = Winery.objects.get(account=self.request.user)
        wine = Wine.objects.filter(winery=winery)
        self.queryset = Review.objects.filter(wine__id__in = wine)
        return super().get_queryset()