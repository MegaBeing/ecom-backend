from rest_framework import viewsets,permissions
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
from .models import Offer, SingleProduct
from .serializers import ProductSerializer, OfferSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = SingleProduct.objects.filter(in_stock=True)
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['get'], name='category')
    def category(self, request):
        category = request.query_params.get('category')
        if category:
            products = self.queryset.filter(product__category=category)
            serializer = self.get_serializer(products, many=True)
            return Response(serializer.data)
        return Response({"error": "Category parameter is required"}, status=400)

    @action(detail=False, methods=['get'], name='filter_by_price')
    def filter_by_price(self, request):
        min_value = int(request.query_params.get('min_value'))
        max_value = int(request.query_params.get('max_value'))
        if min_value and max_value:
            products = self.queryset.filter(price__gte=min_value, price__lte=max_value)
            serializer = self.get_serializer(products, many=True)
            return Response(serializer.data)
        return Response({"error": "Both min_value and max_value are required"}, status=400)

    
    @action(detail=False, methods=['get'], name='filter_by_color')
    def filter_by_color(self, request):
        color = request.query_params.get('color')
        if color:
            products = self.queryset.filter(color=color)
            serializer = self.serializer_class(products, many=True)
            return Response(serializer.data)
        return Response({'error': 'Color parameter is required'}, status=400)

