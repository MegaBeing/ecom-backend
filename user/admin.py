from django.contrib import admin
from .models import User,Cart,CartItem, Address
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number')
    search_fields = ('username', 'email')

admin.site.register(User, UserAdmin)

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Address)
