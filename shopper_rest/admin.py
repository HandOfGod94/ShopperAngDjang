from django.contrib import admin

from .models import Product, Retailer, SaleData


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """admin view for model"""
    list_display = ('id', 'name', 'manufacturer', 'price')


@admin.register(Retailer)
class RetailerAdmin(admin.ModelAdmin):
    """# Retailer admin panel for managing retailer"""
    list_display = ('id', 'name', 'street_address',
                    'locality', 'city', 'contact_no')


@admin.register(SaleData)
class SaleDataAdmin(admin.ModelAdmin):
    """# Product sale data for each retailer on each product"""
    list_display = ('id', 'product_id', 'retailer_id',
                    'bought_quantity', 'sold_quantity')
