from rest_framework import viewsets,permissions
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
from rest_framework import status
from .products_models import SingleProduct, ProductImage
from .products_serializers import ProductSerializer, ProductImageSerializer

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SingleProduct.objects.filter(in_stock=True)
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get']

    @action(detail=False, methods=['get'], url_path='filter')
    def filter_products(self, request):
        search = request.query_params.get('search')
        category = request.query_params.get('category')
        min_value = request.query_params.get('min_value')
        max_value = request.query_params.get('max_value')
        color = request.query_params.get('color')
        collection = request.query_params.get('collection')
        is_exclusive = request.query_params.get('is_exclusive')
        is_best_seller = request.query_params.get('is_best_seller')
        queryset = self.get_queryset()

        if search:
            queryset = queryset.filter(product__name__icontains=search)
        if category:
            queryset = queryset.filter(product__category=category)
        if collection:
            queryset = queryset.filter(product__collection=collection)
        if is_exclusive:
            queryset = queryset.filter(product__isExclusive=True)
        if is_best_seller:
            queryset = queryset.filter(product__isBestSeller=True)
        if min_value:
            queryset = queryset.filter(price__gte=float(min_value))
        if max_value:
            queryset = queryset.filter(price__lte=float(max_value))
        if color:
            queryset = queryset.filter(color=color)

        queryset = queryset.filter(in_stock=True)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    @action(detail=False, methods = ['get'], url_path='new-arrivals')
    def new_arrivals(self, request):
        queryset = self.get_queryset().order_by('-created_at')[:10]
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def best_seller(self, request):
        queryset = self.get_queryset()
        
class ProductImageViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductImageSerializer
    queryset = ProductImage.objects.all()
    permission_classes = [permissions.IsAdminUser]
    http_method_names = ['get']
    