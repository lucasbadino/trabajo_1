from django.urls import path
from alimentos.views import alimentos, lista_alimentos, actualizar_carne, borrar_carnes, form_carne




urlpatterns = [
    path('alimentos/', lista_alimentos, name='alimentos'),
    path('crear-carnes/', form_carne, name = 'crear-carnes'),
    path('editar-carnes/<int:pk>/', actualizar_carne, name= 'editar-carnes'),
    path('borrar-carnes/<int:pk>/', borrar_carnes, name='borrar-carnes'),
]
