from django.db import models
from product.products.products_models import ProductCluster

class Offer(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    active_image = models.ImageField(upload_to='offer')
    product = models.ManyToManyField(ProductCluster,related_name='offer_products')
    
    def __str__(self) -> str:
        return f'{self.name}'

class OfferImage(models.Model):
    alt_name = models.CharField(max_length=25,null=True)
    image = models.ImageField(upload_to='offer')
    offer = models.ForeignKey(Offer,on_delete=models.CASCADE)