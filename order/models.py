from django.db import models
from .constants import OrderStatus,PaymentStatus
# Create your models here.
class Order(models.Model):
    order_id = models.CharField(max_length=50)
    status_code = models.PositiveIntegerField(choices=OrderStatus.choices)
    customer = models.ForeignKey('user.Client', on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=25,choices=PaymentStatus.choices)
    created_at = models.DateTimeField(auto_now_add=True)

