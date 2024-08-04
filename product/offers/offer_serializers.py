from rest_framework import serializers
from .offer_models import Offer
from product.products.products_serializers import ProductClusterSerializer


class OfferSerializer(serializers.ModelSerializer):
    product = ProductClusterSerializer(many=True, read_only=True)
    class Meta:
        model = Offer
        fields = ['id', 'name','is_active', 'image', 'product']
