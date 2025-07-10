from django.urls import path, register_converter, include
from rest_framework import routers
from .api_views import (
    ApplicationViewSet,
)
router = routers.DefaultRouter()

router.register(r'application', ApplicationViewSet, basename='application')

urlpatterns = [
    path('core/', include(router.urls))
]
