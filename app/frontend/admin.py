from .models import Sale
from django.contrib import admin

class SaleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    list_display_links = ('name', 'price', 'description')
    list_per_page = 10


admin.site.register(Sale, SaleAdmin)

# Register your models here.
