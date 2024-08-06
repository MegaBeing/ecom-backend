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

    def create(self, request, *args, **kwargs):
        try:
            client = User.objects.get(pk=self.request.user.pk)
        except User.DoesNotExist:
            return Response({'message': 'User profile not found'}, status=status.HTTP_404_NOT_FOUND)

        if not client.can_order:
            return Response({'message': 'User cannot create orders'}, status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            with transaction.atomic():
                order = serializer.save(
                    client=client,
                    status_code=0,
                    payment_status=request.data.get('payment_status')
                )

                # Shiprocket API call (commented out for now)
                """
                shiprocket_payload = {
                    # Construct your Shiprocket payload here
                }
                headers = {
                    'Authorization': f'Bearer {self.SHIPROCKET_API_TOKEN}',
                    'Content-Type': 'application/json'
                }
                response = requests.post(SHIPROCKET_URLS['CREATE_ORDER'], json=shiprocket_payload, headers=headers)
                if response.status_code == 200:
                    order_data = response.json()
                    order.order_id = order_data.get('order_id')
                    order.shipment_id = order_data.get('shipment_id')
                    order.save()
                else:
                    raise Exception('Failed to create Shiprocket order')
                """

                return Response({'message': 'Order Created', 'order_id': order.id}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'message': f'Cannot complete the transaction. Error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
