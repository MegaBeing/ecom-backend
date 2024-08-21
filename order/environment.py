import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

API_AUTH = {
    'SHIPROCKET_API_TOKEN':os.getenv('SHIPROCKET_API_TOKEN')
}

SHIPROCKET_URLS = {
    'CREATE_ORDER':'https://apiv2.shiprocket.in/v1/external/orders/create/adhoc',
    'GET_TRACKING':'https://apiv2.shiprocket.in/v1/external/courier/track/shipment/' # LAST MUST BE SHIPMENT ID
}

SHIPROCKET_REQ_HEADER = {
    'Content-Type': 'application/json',
    'Authorization':API_AUTH.get('SHIPROCKET_API_TOKEN'),
}

CUSTOM_ORDER_PAYLOAD = {
            "order_id": "",
            "order_date": "",
            "pickup_location": "",
            "channel_id": "",
            "comment": "",
            "billing_customer_name": "",
            "billing_last_name": "",
            "billing_address": "",
            "billing_address_2": "",
            "billing_city": "",
            "billing_pincode": "",
            "billing_state": "",
            "billing_country": "",
            "billing_email": "",
            "billing_phone": "",
            "shipping_is_billing": True,
            "order_items": [],
            "payment_method": "",
            "shipping_charges": 0,
            "giftwrap_charges": 0,
            "transaction_charges": 0,
            "total_discount": 0,
            "sub_total": 0,
            "length": 0,
            "breadth": 0,
            "height": 0,
            "weight": 0
        }

USER_KEY_TO_APIKEY = {
    "billing_customer_name": "first_name",
    "billing_last_name": "last_name",
    "billing_address": "address_line1",
    "billing_address_2": "address_line2",
    "billing_city": "city",
    "billing_pincode": "pincode",
    "billing_state": "state",
    "billing_country": "country",
    "billing_email": "email_id",
    "billing_phone": "phone",
}
ORDERED_ITEMS_KEY_TO_APIKEY = {
    "name": "name",
    "sku": "id",
    "units": "quantity",
    "selling_price": "price",
    # Discount can be directly calculated using previous price and selling price
}