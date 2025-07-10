from .models import (
    Application,
)
from .serializers import (
    ApplicationReadSerializer, ApplicationWriteSerializer,
)

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_condition import And, Or
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, OAuth2Authentication
from rest_framework.authentication import SessionAuthentication
from .pagination import CustomPagination
from rest_framework import generics
from rest_framework import filters
import django_filters.rest_framework


class ApplicationViewSet(ModelViewSet):
    queryset = Application.objects.all()
    pagination_class = CustomPagination
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = permission_classes = [Or(IsAdminUser, TokenHasReadWriteScope)]
    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter,
        django_filters.rest_framework.DjangoFilterBackend
    )
    filterset_fields = '__all__'
    search_fields = ['github', 'repository']
    ordering_fields = '__all__'
    ordering = ["id"]
    
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ApplicationReadSerializer
        return ApplicationWriteSerializer
