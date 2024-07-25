from django.contrib import admin
from .products.products_models import ProductCluster, SingleProduct
from .offers.offer_models import Offer
from .admin_range.range import IntegerRangeFilter
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_filter = (IntegerRangeFilter,)
    list_display = ['get_name','get_category','in_stock', 'color',]

    def get_name(self, obj):
        return obj.product.name
    get_name.short_description = 'Product Name'
    get_name.admin_order_field ='product__name'
    
    def get_category(self, obj):
        return obj.product.category
    get_category.short_description = 'Product Category'
    get_category.admin_order_field ='product__category'
admin.site.register(SingleProduct,ProductAdmin)
admin.site.register(Offer)

class ProductClusterAdmin(admin.ModelAdmin):
    list_display = ['name','category']
admin.site.register(ProductCluster,ProductClusterAdmin)