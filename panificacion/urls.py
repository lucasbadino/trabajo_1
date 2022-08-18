from django.urls import path
from panificacion.views import *



urlpatterns = [
    path('panes/', lista_panes, name= 'panes'),
    path('crear-panes/', form_panes, name = 'crear-panes'),
    path('editar-panes/<int:pk>/', actualizar_panes, name='editar-panes'),
    path('borrar-panes/<int:pk>/', borrar_panes, name='borrar-panes'),
]
