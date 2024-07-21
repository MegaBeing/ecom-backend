from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=100)
    image = models.ImageField()
    previous_price = models.PositiveIntegerField(blank=True)
    # dimensions
    length = models.FloatField()
    breath = models.FloatField()
    height = models.FloatField()
    color = models.CharField(max_length=10)
    # related fields
    by_color = models.ManyToManyField(
            'self',
            blank=True
        )
    by_size = models.ManyToManyField(
        'self',
        blank=True
    )
    def __str__(self) -> str:
        return f'{self.name}'
    @property
    def dimensions(self):
        return f'{self.length}x{self.breath}x{self.height}'

class Offer(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    image = models.ImageField(upload_to=None)
    product = models.ManyToManyField(Product)

