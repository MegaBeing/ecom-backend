from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .models import Order
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderSerializer
from .environment import API_AUTH,SHIPROCKET_URLS,SHIPROCKET_REQ_HEADER
from user.models import User
import requests
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    SHIPROCKET_API_TOKEN = API_AUTH['SHIPROCKET_API_TOKEN']

    def get_queryset(self):
        return self.queryset.filter(client=self.request.user)