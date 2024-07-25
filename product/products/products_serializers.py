from rest_framework import serializers
from .products_models import SingleProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleProduct
        fields = '__all__'
