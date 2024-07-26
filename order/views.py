from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .models import Order
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderSerializer
class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset
    
