
from django.contrib import admin
from meat.models import Products



@admin.register(Products)
class Products_admin(admin.ModelAdmin):
    list_display=['id','name','sku',  'price', 'stock', 'image']