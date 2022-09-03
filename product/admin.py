from django.contrib import admin
from product.models import Products

# Register your models here.
@admin.register(Products)
class Products_admin(admin.ModelAdmin):
    list_display=['id','name', 'price', 'stock', 'image', 'category']
    
