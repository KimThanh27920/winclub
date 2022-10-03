from rest_framework import generics

from . import serializers
from reviews.models import Review
from wines.models import Wine


class ListReviewsAPIView(generics.ListAPIView):
    serializer_class = serializers.ReviewSerializer

    def get_queryset(self):
        wine_id = self.request.data.get("wine")
        wine = Wine.objects.get(id=wine_id)
        self.queryset = Review.objects.filter(wine=wine)
        return super().get_queryset()