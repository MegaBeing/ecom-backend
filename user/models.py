from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from product.models import SingleProduct
class Address(models.Model):
    pincode = models.PositiveIntegerField(null=False)
    address_line1 = models.CharField(max_length=200, null=False)
    address_line2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=100, null=False)

class Cart(models.Model):
    items = models.ManyToManyField(SingleProduct)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    
class Client(User): 
    can_order = models.BooleanField(default=False)
    phone_number = models.CharField(validators=[MinLengthValidator(10)], max_length=15,null=True)
    shipping_address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='client_address', null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    class Meta:
        verbose_name = 'Client'
    
class Location(models.Model):
    name = models.CharField(max_length=50, null=False)
    state_id = models.CharField(max_length = 50)
    state_code = models.CharField(max_length = 50)
    state_name = models.CharField(max_length = 50)
    country_id = models.CharField(max_length = 50)
    country_code = models.CharField(max_length = 50)
    country_name = models.CharField(max_length = 50)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    wikiDataId = models.CharField(max_length = 50, null=True)