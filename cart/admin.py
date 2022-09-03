
from django.contrib import admin
from cart.models import Prueba

# Register your models here.
@admin.register(Prueba)
class Prueba_admin(admin.ModelAdmin):
    list_display=['todos_productos' ]