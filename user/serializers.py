from rest_framework.serializers import ModelSerializer,IntegerField
from .models import Client,Address,Cart,CartItem
from product.products.products_serializers import ProductSerializer
class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ['username', 'email', 'phone_number','shipping_address']
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
        
class ClientAddressSerializer(ModelSerializer):
    shipping_address = AddressSerializer()
    class Meta:
        model = Client
        fields = ['shipping_address']
    
    def create(self, validated_data):
        shipping_address = validated_data.pop('shipping_address')
        client = Client.objects.create(**validated_data)
        client.shipping_address = Address.objects.create(**shipping_address)
        client.save()
        return client
    
    def update(self, instance, validated_data):
        shipping_address_data = validated_data.pop('shipping_address')
        if shipping_address_data:
            shipping_address = instance.shipping_address
            for attr, value in shipping_address_data.items():
                setattr(shipping_address, attr, value)
            shipping_address.save()
        return instance
    
    
class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

