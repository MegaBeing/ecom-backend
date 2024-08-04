from rest_framework import serializers
from .products_models import SingleProduct, ProductImage, ProductCluster


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'image')
class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model = SingleProduct
        fields = ['id','product', 'price', 'description', 'previous_price', 'dimensions', 'color', 'images']

class ProductClusterSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = ProductCluster
        fields = ['id','name','category','product']