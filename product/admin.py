from django.contrib import admin
from .products.products_models import ProductCluster, SingleProduct, ProductImage
from .offers.offer_models import Offer
from .admin_range.range import IntegerRangeFilter
# Register your models here.
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
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


class OfferAdmin(admin.ModelAdmin):
    list_display = ['name','is_active']
    filter_horizontal = ('product',)
admin.site.register(Offer, OfferAdmin)

class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['alt_text','image']
admin.site.register(ProductImage,ProductImageAdmin)
class ProductClusterAdmin(admin.ModelAdmin):
    list_display = ['name','category']
admin.site.register(ProductCluster,ProductClusterAdmin)