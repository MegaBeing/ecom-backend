from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from product.products.products_models import ProductCluster,SingleProduct

class User(AbstractUser): 
    is_active = models.BooleanField(default=True)
    phone_number = models.CharField(validators=[MinLengthValidator(10)], max_length=15,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    
    def __str__(self) -> str:
        return f'{self.first_name} - {self.last_name if self.last_name else self.email}'
    class Meta:
        permissions = [('can_order', 'can place orders'),]
class Address(models.Model):
    pincode = models.PositiveIntegerField(null=False)
    address_line1 = models.CharField(max_length=200, null=False)
    address_line2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
class Reviews(models.Model):
    rating = models.PositiveIntegerField(null=False)
    description = models.TextField(null=True)
    product = models.ForeignKey(ProductCluster, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self) -> str:
        return f'{self.product.name} - {self.rating}'
    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

class Cart(models.Model):
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    client = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    
    def __str__(self) -> str:
        return f'{self.client.id} - ₹ {self.total_amount}'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,related_name='cart_items')
    product = models.ForeignKey(SingleProduct, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    
    
