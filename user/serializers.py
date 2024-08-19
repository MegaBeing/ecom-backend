from rest_framework.serializers import ModelSerializer
from .models import User,Address,Cart,CartItem
from product.products.products_serializers import ProductSerializer
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
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
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
