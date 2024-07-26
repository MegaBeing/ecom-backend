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
