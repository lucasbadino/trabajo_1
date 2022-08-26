

from django.contrib import admin
from drink.models import Drinks



@admin.register(Drinks)
class Drinks_admin(admin.ModelAdmin):
    list_display=['id','name','sku',  'price', 'stock', 'image']
