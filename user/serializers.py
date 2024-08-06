from rest_framework.serializers import ModelSerializer
from .models import User,Address,Cart
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name', 'username','email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = self.Meta.model(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user
    
class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
        
class UserAddressSerializer(ModelSerializer):
    shipping_address = AddressSerializer()
    class Meta:
        model = User
        fields = ['shipping_address']
    
    def create(self, validated_data):
        shipping_address = validated_data.pop('shipping_address')
        client = User.objects.create(**validated_data)
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

