from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserAddressViewSet,CartViewSet,UserLoginView,UserSignUpView

router = DefaultRouter()
router.register('user_address',UserAddressViewSet, basename='clientaddress')
router.register('cart',CartViewSet, basename='cart')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', UserLoginView.as_view(), name='login'  ),
    path('signup/',UserSignUpView.as_view(), name='signup'  ),
]