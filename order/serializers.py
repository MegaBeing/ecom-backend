from rest_framework.serializers import ModelSerializer
from user.models import User
from .models import Order
from .environment import API_AUTH,SHIPROCKET_URLS,SHIPROCKET_REQ_HEADER,CUSTOM_ORDER_PAYLOAD
import json
import requests
class OrderSerializer(ModelSerializer):
    SHIPROCKET_API_TOKEN = API_AUTH['SHIPROCKET_API_TOKEN']
    class Meta:
        model = Order
        fields = "__all__"
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        # changes when we integrate with Shiprocket
        '''
        custom_order_payload = CUSTOM_ORDER_PAYLOAD
        headers = SHIPROCKET_REQ_HEADER
        url = SHIPROCKET_URLS['CREATE_ORDER']
        response = requests.request("POST", 
                                    url , 
                                    headers=headers, 
                                    data=custom_order_payload
                                )
        '''
        return super().create(validated_data)
