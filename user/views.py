from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.decorators import action
from .models import User, Cart , CartItem
from product.products.products_models import SingleProduct
from .serializers import UserSerializer, UserAddressSerializer, CartSerializer 
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
        
        
class UserAddressViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserAddressSerializer
    permission_classes = [permissions.IsAuthenticated,]
    
    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset
        if user.is_authenticated:
            return queryset.filter(pk=user.pk)
        else:
            return queryset.none()
    
    @action(detail=True, methods=['POST'])
    def create_address(self,request,pk=None):
        user = self.get_queryset()
        data = request.data 
        serializer = self.serializer_class(user, data = data, partial = True)
        if serializer.is_valid():
            try:
                with transaction.atomic():
                    serializer.save()
                return Response({'message':'Address Created'},status = status.HTTP_200_OK)
            except Exception as e:
                return Response({'message':f'Error creating address for the user: {str(e)}'},status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['PUT'])
    def update_address(self, request, pk=None):
        user = self.get_queryset()
        data = request.data 
        serializer = self.serializer_class(user, data = data, partial = True)
        if serializer.is_valid():
            try:
                with transaction.atomic():
                    serializer.save()
                return Response({'message': 'Shipping address updated successfully'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'message': f'Error updating the shipping address: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class CartViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CartSerializer
    def get_queryset(self):
        return Cart.objects.filter(client=self.request.user)
    
    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.first()
        if not obj:
            obj = Cart.objects.create(client=self.request.user)
        return obj

    @action(detail=False, methods=['post'],url_path='add-to-cart')
    def add_to_cart(self, request):
        cart = self.get_object()
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity')

        if not product_id or not quantity:
            return Response({'message': 'Invalid request. Please provide product_id and quantity.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            quantity = int(quantity)
            if quantity <= 0:
                return Response({'message': 'Quantity must be a positive integer.'}, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response({'message': 'Quantity must be a valid integer.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = SingleProduct.objects.get(pk=product_id,in_stock=True)
        except SingleProduct.DoesNotExist:
            return Response({'message': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)
        try:
            cart_item = CartItem.objects.get(cart=cart, product=product)
            try:
                with transaction.atomic():
                    cart_item.quantity += 1
                    cart_item.total_amount += product.price
                    cart.total_amount += product.price
                    cart_item.save()
                    cart.save()
                return Response({'message': 'Cart Product Quantity Incremented'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'message': f'Error Incrementing Cart Product Quantity: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except CartItem.DoesNotExist: 
            try:
                with transaction.atomic():
                    cart_item = CartItem.objects.create(
                        cart=cart, 
                        product=product,
                        quantity=quantity,
                        total_amount=product.price * quantity
                    )
                    cart.total_amount += cart_item.total_amount
                    cart.save()
                return Response({'message': 'Product added to cart successfully'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'message': f'Error adding product to cart: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @action(detail=False, methods=['delete'],url_path='remove-from-cart')
    def remove_from_cart(self, request):
        cart = self.get_object()
        product_id = request.data.get('product_id')

        if not product_id:
            return Response({'message': 'Invalid request. Please provide product_id.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = SingleProduct.objects.get(pk=product_id)
        except SingleProduct.DoesNotExist:
            return Response({'message': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)

        try:
            cart_item = CartItem.objects.get(cart=cart, product=product)
        except CartItem.DoesNotExist:
            return Response({'message': 'No such item found in cart'}, status=status.HTTP_404_NOT_FOUND)

        try:
            with transaction.atomic():
                if(cart_item.quantity > 1):
                    cart_item.quantity -= 1
                    cart_item.total_amount -= product.price
                    cart.total_amount -= product.price
                    cart_item.save()
                    cart.save()
                else:
                    cart_item.delete()
            return Response({'message': 'Cart item deleted'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': f'Error deleting the cart item: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)