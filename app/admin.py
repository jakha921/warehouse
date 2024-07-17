import openpyxl
from django.contrib import admin
from django.http import HttpResponse
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from app.models import Reception, Product, Warehouse, Transmitting, Staff, Department, Debt

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
    date_hierarchy = 'receiver_date'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    ordering = ['name']
    list_per_page = 15


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    ordering = ['name']
    list_per_page = 15


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['product', 'count']
    search_fields = ['product__name']
    autocomplete_fields = ['product']
    ordering = ['product']
    list_per_page = 15
    # list_max_show_all = 100

    actions = ['export_inventory_to_excel']

    # action download csv file
    def download_csv(modeladmin, request, queryset):
        import csv
        from django.http import HttpResponse
        import io

        f = io.StringIO()
        writer = csv.writer(f)
        writer.writerow(['product', 'count'])
        for s in queryset:
            writer.writerow([s.product, s.count])
        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=warehouse.csv'
        return response


    def export_inventory_to_excel(modeladmin, request, queryset):
        # Create an in-memory workbook
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = 'Room Inventory'

        # Add header row
        headers = ['Inventar', 'Inventar soni']
        sheet.append(headers)

        # Add data rows
        for warehouse in queryset:
            row = [
                warehouse.product.name,
                warehouse.count,
            ]
            sheet.append(row)

        # Set the response as an Excel file
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename=warehouse_inventory.xlsx'
        workbook.save(response)
        return response

    export_inventory_to_excel.short_description = "Excel-ga tanlangan inventarlarini yuklash"


@admin.register(Transmitting)
class TransmittingAdmin(admin.ModelAdmin):
    list_display = ['staff', 'product', 'count']
    search_fields = ['product__name', 'staff__name', 'comment', 'department__name']
    autocomplete_fields = ['product', 'staff']
    list_per_page = 15


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['name', 'department', 'position', 'phone']
    search_fields = ['name', 'position']
    ordering = ['name']
    autocomplete_fields = ['department']
    list_per_page = 15


@admin.register(Debt)
class DebtAdmin(admin.ModelAdmin):
    list_display = ['name', 'debt_amount', 'comment']
    search_fields = ['name', 'comment']

    # ordering = ['name']

    # def image_preview(self, obj):
    #     if obj.image:
    #         print('obj.photo.url', obj.image.url)
    #         return format_html(f'<img src="{obj.image.url}" width="85" height="55" />')
    #     return 'Rasm yo`q'
    #
    # image_preview.short_description = 'Rasm'
