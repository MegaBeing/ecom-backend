from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.decorators import action
from .models import User, Cart , CartItem, Address
from product.products.products_models import SingleProduct
from .serializers import UserSerializer, AddressSerializer, CartSerializer
from rest_framework import permissions
from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class UserLoginView(APIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({'message': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(email=email).first()

        if user is None or not user.check_password(password):
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
            
        return Response({
            'message': 'Logged in successfully',
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
        }, status=status.HTTP_200_OK)

class UserSignUpView(APIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            with transaction.atomic():
                user = serializer.save()
                refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'User Created',
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
            }, status=status.HTTP_201_CREATED)
        except serializer.ValidationError as e:
            return Response({'message': 'Validation error', 'errors': e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': f'Error creating user: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    
    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset
        if user.is_authenticated:
            return queryset.filter(user=user)
        else:
            return queryset.none()
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

class CartViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CartSerializer
    def get_queryset(self):
        return Cart.objects.filter(client=self.request.user)
    
    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.first()
        if not obj:
            try: 
                with transaction.atomic():
                    obj = Cart.objects.create(client=self.request.user)
            except Exception as e:
                return Response({'message': f'Error creating cart for the user: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return obj

    @action(detail=False, methods=['POST'],url_path='add-to-cart')
    def add_to_cart(self, request):
        cart = self.get_object()
        product_id = request.data.get('product_id')
        
        if not product_id:
            return Response({'message': 'Product id is required'}, status=status.HTTP_400_BAD_REQUEST)
        product = SingleProduct.objects.filter(id=product_id).first()
        
        if not product:
            return Response({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product = product)
        if created:
            try: 
                with transaction.atomic():
                    cart_item.quantity = 1
                    cart_item.total_amount += product.price
                    cart_item.save()
                    cart.total_amount += cart_item.product.price
                    cart.save()
                return Response({'message': 'Product added to cart'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'message': f'Error adding product to cart: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            try:
                with transaction.atomic():
                    cart_item.quantity += 1
                    cart_item.total_amount += product.price
                    cart_item.save()
                    cart.total_amount += cart_item.product.price
                    cart.save()
                return Response({'message': 'Product quantity increased in cart'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'message': f'Error increasing product (id:{product_id}) quantity in cart: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @action(detail=False, methods=['DELETE'],url_path='remove-from-cart')
    def remove_from_cart(self, request):
        cart  = self.get_object()
        product_id = request.data.get('product_id')
        if not product_id:
            return Response({'message': 'Product id is required'}, status=status.HTTP_400_BAD_REQUEST)
        product = SingleProduct.objects.filter(id=product_id).first()
        if not product: 
            return Response({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        cart_item = CartItem.objects.filter(cart=cart, product = product).first()
        if not cart_item:
            return Response({'message': 'Product not found in cart'}, status=status.HTTP_404_NOT_FOUND)
        try: 
            with transaction.atomic():
                if cart_item.quantity == 1:
                    cart_item.delete()
                    cart.total_amount -= product.price
                    cart.save()
                else:
                    cart_item.quantity -= 1
                    cart_item.total_amount -= product.price
                    cart_item.save()
                    cart.total_amount -= product.price
                    cart.save()
            return Response({'message':'Decremented or Removed from the cart'},status=status.HTTP_200_OK)
        except Exception as e:
                return Response({'message': f'Error Decreasing/Removing product (id:{product_id}) quantity from the cart: {str(e)}'},status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
                    