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
    product_outer_material = serializers.CharField(source='product.outer_material')
    product_inner_material = serializers.CharField(source='product.inner_material')
    product_sling = serializers.BooleanField(source='product.sling')
    product_closer = serializers.BooleanField(source='product.closer')
    product_pocket = serializers.BooleanField(source='product.pocket')
    images = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model = SingleProduct
        fields = ['id','product_name', 'product_category','product_collection',
                  'product_outer_material','product_inner_material','product_sling',
                  'product_closer','product_pocket',
                  'price', 'description', 'previous_price', 'dimensions', 'color', 'images'
                  ]             
class ProductClusterSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = ProductCluster
        fields = ['id','name','category','product']