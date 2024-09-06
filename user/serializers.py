from rest_framework.serializers import ModelSerializer
from .models import User,Address,Cart,CartItem
from product.products.products_serializers import ProductSerializer
from rest_framework import status
from rest_framework.response import Response
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
        fields = ['id','type','billing_address_name','billing_address_phone',
                  'address_line1','address_line2',
                  'city','state','country','pincode']
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        # check address count 
        address_count = Address.objects.filter(user = self.context['request'].user).count()
        if address_count == 3:
            return Response({'message': 'Address Creation Limit Reached'},status=status.HTTP_401_UNAUTHORIZED)
        return super().create(validated_data)
class CartItemSerializer(ModelSerializer):
    product = ProductSerializer(many=False)
    class Meta:
        model = CartItem
        fields = ['id','quantity','total_amount','product']
class CartSerializer(ModelSerializer):
    cart_items = CartItemSerializer(many=True,read_only=True)
    class Meta:
        model = Cart
        fields = ['id','client','total_amount', 'cart_items']
