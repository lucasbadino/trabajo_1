from django.contrib import admin

from django.contrib import admin
from contact.models import Contact



@admin.register(Contact)
class Contact_admin(admin.ModelAdmin):
    list_display=['nombre','email',  'tipo_de_consulta', 'comentario','notificaciones','telefono']

