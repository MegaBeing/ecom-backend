from django.db import models
from .constants import ProductCategory
class ProductCluster(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(choices=ProductCategory.choices, max_length=50,default='Clutch bag')
    
    def __str__(self) -> str:
        return f'{self.name} - {self.category}'
    class Meta:
        verbose_name = 'Product Cluster'

class SingleProduct(models.Model):
    product = models.ForeignKey(ProductCluster, on_delete=models.CASCADE, related_name='product',null = True)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=100)
    image = models.ImageField()
    previous_price = models.PositiveIntegerField(blank=True,null=True)
    
    # dimensions
    length = models.FloatField()
    breath = models.FloatField()
    height = models.FloatField()
    
    # product details
    color = models.CharField(max_length=10)
    in_stock = models.BooleanField(default=True)
    
    # properties
    def __str__(self) -> str:
        return f'{self.product.name} - [{self.color}, {self.price}]'
    @property
    def dimensions(self):
        return f'{self.length}x{self.breath}x{self.height}'
    
    class Meta:
        verbose_name = 'Single Product'

class Offer(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    image = models.ImageField(upload_to=None)
    product = models.ManyToManyField(ProductCluster)

