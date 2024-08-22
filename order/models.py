from django.db import models
from .constants import OrderStatus,PaymentStatus
# Create your models here.
class Order(models.Model):
    shipment_id = models.CharField(max_length=50)
    order_id = models.CharField(max_length=50)
    status_code = models.IntegerField(choices=OrderStatus.choices)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=25,choices=PaymentStatus.choices,default='pending')
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    cart = models.ForeignKey('user.Cart', on_delete=models.CASCADE,null=True)