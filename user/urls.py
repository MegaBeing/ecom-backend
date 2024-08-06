from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserViewSet,UserAddressViewSet,CartViewSet

router = DefaultRouter()
router.register('user',UserViewSet, basename='user')
router.register('UserAddress',UserAddressViewSet, basename='clientaddress')
router.register('cart',CartViewSet, basename='cart')

urlpatterns = [
    path('', include(router.urls)),
]