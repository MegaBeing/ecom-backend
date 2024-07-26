from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ClientViewSet,ClientAddressViewSet,CartViewSet

router = DefaultRouter()
router.register('client',ClientViewSet, basename='client')
router.register('ClientAddress',ClientAddressViewSet, basename='clientaddress')
router.register('cart',CartViewSet, basename='cart')

urlpatterns = [
    path('', include(router.urls)),
]