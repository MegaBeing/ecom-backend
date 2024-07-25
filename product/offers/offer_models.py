from django.db import models
from product.products.products_models import ProductCluster

class Offer(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    image = models.ImageField(upload_to=None)
    product = models.ManyToManyField(ProductCluster)
