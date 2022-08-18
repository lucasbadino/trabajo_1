from django.urls import path
from bebidas.views import bebidas,  lista_bebidas, actualizar_bebidas, borrar_bebidas, form_bebidas




urlpatterns = [
    path('bebidas/', lista_bebidas, name='bebidas'),
    path('crear-bebidas/', form_bebidas, name = 'crear-bebidas'),
    path('editar-bebidas/<int:pk>/', actualizar_bebidas, name='editar-bebidas'),
    path('borrar-bebidas/<int:pk>/', borrar_bebidas, name='borrar-bebidas'),
]
