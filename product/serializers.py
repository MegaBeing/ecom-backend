from rest_framework import serializers
from .models import Offer, SingleProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleProduct
        fields = '__all__'

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'