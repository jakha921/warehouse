from django.contrib import admin

from app.models import Reception, Product, Warehouse, Transmitting

# Register your models here.
admin.site.site_header = 'Mahsulotlar ombori'
admin.site.site_title = 'Mahsulotlar ombori'
admin.site.index_title = 'Mahsulotlar ombori'


@admin.register(Reception)
class ReceptionAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_count', 'product_price', 'sender', 'receiver', 'receiver_date']
    search_fields = ['product_name', 'sender', 'receiver']
    ordering = ['-receiver_date']
    list_per_page = 15
    list_max_show_all = 100
    date_hierarchy = 'receiver_date'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    ordering = ['name']
    list_per_page = 15
    list_max_show_all = 100


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['product', 'count']
    search_fields = ['product__name']
    autocomplete_fields = ['product']
    ordering = ['product']
    list_per_page = 15
    list_max_show_all = 100


@admin.register(Transmitting)
class TransmittingAdmin(admin.ModelAdmin):
    list_display = ['receiver', 'product', 'count']
    search_fields = ['product__name', 'receiver', 'comment', 'department']
    autocomplete_fields = ['product']
    list_per_page = 15
    list_max_show_all = 100
