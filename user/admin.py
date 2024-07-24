from django.contrib import admin
from .models import Client
# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'can_order', 'phone_number')
    list_filter = ('can_order',)

admin.site.register(Client, ClientAdmin)

