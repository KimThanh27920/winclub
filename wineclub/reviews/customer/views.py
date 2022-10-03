from rest_framework_simplejwt import authentication
from rest_framework import generics, status, permissions
from rest_framework.response import Response

from . import serializers
from reviews.models import Review


class CreateReviewAPIView(generics.ListCreateAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return serializers.ListReviewsSerializer
        else:
            return serializers.ReviewSerializer

    def get_queryset(self):
        self.queryset = Review.objects.filter(created_by=self.request.user)
        return super().get_queryset()

    def post(self, request, *args, **kwargs):
        try:
            serializer = serializers.ReviewSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(created_by=self.request.user, updated_by=self.request.user)

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UpdateReviewAPIView(generics.UpdateAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.UpdateReviewSerializer
    lookup_url_kwarg = 'review_id'

    def get_queryset(self):
        self.queryset = Review.objects.filter(created_by=self.request.user)
        return super().get_queryset()

    def update(self, request, *args, **kwargs):
        review = self.get_object()
        if request.user == review.created_by:
            review_content = self.request.data.get('content')
            review.content = review_content
            review.save()

            return super().update(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)
