from django.contrib import admin
from .models import Product, Offer
from .admin_range.range import IntegerRangeFilter
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_filter = (IntegerRangeFilter,)
    list_display = ('name','price','dimensions')

admin.site.register(Product,ProductAdmin)
admin.site.register(Offer)