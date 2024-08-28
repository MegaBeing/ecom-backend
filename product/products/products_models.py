from django.db import models
from .products_constants import ProductCategory,CollectionCategory
class ProductCluster(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(choices=ProductCategory.choices, max_length=50,default='Clutch bag')
    collection = models.CharField(choices=CollectionCategory.choices, max_length=50, default='indian')
    isExclusive = models.BooleanField(default=False)
    def __str__(self) -> str:
        return f'{self.name} - {self.category}'
    class Meta:
        verbose_name = 'Product Cluster'

class SingleProduct(models.Model):
    product = models.ForeignKey(ProductCluster, on_delete=models.CASCADE, related_name='product',null = True)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=500)
    previous_price = models.PositiveIntegerField(blank=True,null=True)
    
    # dimensions
    length = models.FloatField()
    breath = models.FloatField()
    height = models.FloatField()
    
    # product details
    color = models.CharField(max_length=10)
    in_stock = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    # properties
    def __str__(self) -> str:
        return f'{self.product.name} - [{self.color}, {self.price}]'
    @property
    def dimensions(self):
        return f'{self.length}x{self.breath}x{self.height}'
    
    class Meta:
        verbose_name = 'Single Product'
class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_images/')
    products = models.ForeignKey(SingleProduct, related_name='images', on_delete=models.CASCADE)
    alt_text = models.CharField(max_length=100, blank=True)
    
    def __str__(self) -> str:
        return f'{self.alt_text}'
    
