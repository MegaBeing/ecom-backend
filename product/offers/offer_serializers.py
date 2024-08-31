from rest_framework import serializers
from .offer_models import Offer, OfferImage
from product.products.products_serializers import ProductClusterSerializer

class OfferImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url = True)
    class Meta:
        model = OfferImage
        fields = ['alt_name','image']
class OfferSerializer(serializers.ModelSerializer):
    product = ProductClusterSerializer(many=True, read_only=True)
    image = OfferImageSerializer(many=True,read_only=True)
    class Meta:
        model = Offer
        fields = ['id', 'name','is_active', 'active_image','image', 'product']
