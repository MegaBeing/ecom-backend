from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .models import Order
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderSerializer
from user.models import User
import requests
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'delete', 'head', 'options']
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
