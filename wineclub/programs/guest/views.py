# From rest_framework
from rest_framework import generics, filters
from rest_framework_simplejwt import authentication
from django_filters.rest_framework import DjangoFilterBackend
# From app
from .serializers import  RewardProgramReadSerializer, RewardProgramReadDetailSerializer
from ..models import RewardProgram



class ProgramListView(generics.ListAPIView):
    serializer_class = RewardProgramReadSerializer
    authentication_classes = [authentication.JWTAuthentication]
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['created_by__wineries__name', 'created_by__wineries__id', 'created_by__email']
    ordering = ['-created_at']
        
    def get_queryset(self):
        self.queryset = RewardProgram.objects.filter(deleted_by=None, is_active=True)
        return self.queryset
        
        
class RetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = RewardProgramReadDetailSerializer
    authentication_classes = [authentication.JWTAuthentication]
    lookup_url_kwarg = 'program_id'
    
    def get_queryset(self):
        queryset = RewardProgram.objects.filter(deleted_by=None, is_active=True)
        return queryset
    
   