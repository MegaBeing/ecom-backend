from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import AddressViewSet,CartViewSet,UserLoginView,UserSignUpView
from rest_framework_simplejwt.views import  TokenRefreshView , TokenVerifyView
router = DefaultRouter()
router.register('user_address',AddressViewSet, basename='clientaddress')
router.register('cart',CartViewSet, basename='cart')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', UserLoginView.as_view(), name='login'  ),
    path('signup/',UserSignUpView.as_view(), name='signup' ),
    path('verify/', TokenVerifyView.as_view(), name='token-verify'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh')
]