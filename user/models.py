from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from product.products.products_models import ProductCluster,SingleProduct

class Address(models.Model):
    pincode = models.PositiveIntegerField(null=False)
    address_line1 = models.CharField(max_length=200, null=False)
    address_line2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Client(User): 
    can_order = models.BooleanField(default=False)
    phone_number = models.CharField(validators=[MinLengthValidator(10)], max_length=15,null=True)
    shipping_address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='client_address', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Client'
class Reviews(models.Model):
    rating = models.PositiveIntegerField(null=False)
    description = models.TextField(null=True)
    product = models.ForeignKey(ProductCluster, on_delete=models.CASCADE)
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

class Cart(models.Model):
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(SingleProduct, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    
