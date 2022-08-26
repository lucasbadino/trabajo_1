
from django.contrib import admin
from bakery.models import Bakeries



@admin.register(Bakeries)
class Bakeries_admin(admin.ModelAdmin):
    list_display=['id','name','sku',  'price', 'stock', 'image']