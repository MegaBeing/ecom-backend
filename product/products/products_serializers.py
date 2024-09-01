from rest_framework import serializers
from .products_models import SingleProduct, ProductImage, ProductCluster


class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url = True)
    class Meta:
        model = ProductImage
        fields = ('id', 'image')
class ProductSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name')
    product_category = serializers.CharField(source='product.category')
    product_collection = serializers.CharField(source='product.collection')
    images = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model = SingleProduct
        fields = ['id','product_name', 'product_category','product_collection','price', 'description', 'previous_price', 'dimensions', 'color', 'images']

class ProductClusterSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = ProductCluster
        fields = ['id','name','category','product']