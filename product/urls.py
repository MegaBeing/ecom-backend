from django.urls import path,include
from rest_framework import routers
from product.products.products_viewset import ProductViewSet
from product.offers.offer_viewsets import OfferViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='singleproduct')
router.register(r'offers', OfferViewSet, basename='offer')

urlpatterns = [
    path('', include(router.urls)),
]
