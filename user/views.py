from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .models import Client, Cart , CartItem
from product.products.products_models import SingleProduct
from .serializers import ClientSerializer, ClientAddressSerializer, CartSerializer ,CartItemSerializer
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset
        if user.is_authenticated:
            return queryset.filter(pk=user.pk)
        else:
            return queryset.none()
        
class ClientAddressViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientAddressSerializer
    permission_classes = [IsAuthenticated]
    
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
    permission_classes = [IsAuthenticated]
    serializer_class = CartSerializer
    
    def get_queryset(self):
        return Cart.objects.filter(client=self.request.user)
    
    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.first()
        if not obj:
            obj = Cart.objects.create(client=self.request.user)
        return obj

    @action(detail=False, methods=['POST'])
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
            product = SingleProduct.objects.get(pk=product_id)
        except SingleProduct.DoesNotExist:
            return Response({'message': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)

        try:
            with transaction.atomic():
                cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
                cart_item.quantity += quantity
                cart_item.save()
            return Response({'message': 'Product added to cart successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': f'Error adding product to cart: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @action(detail=False, methods=['POST'])
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
                cart_item.delete()
            return Response({'message': 'Cart item deleted'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': f'Error deleting the cart item: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)