"""coderstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from coderstore.views import inicio, buscar_productos
from alimentos.views import alimentos, lista_alimentos, actualizar_carne, borrar_carnes, form_carne
from bebidas.views import bebidas, lista_bebidas, actualizar_bebidas, borrar_bebidas, form_bebidas
from panificacion.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('alimentos/', lista_alimentos, name='alimentos'),
    path('bebidas/', lista_bebidas, name='bebidas'),
    path('panes/', lista_panes, name= 'panes'),
    path('crear-carnes/', form_carne, name = 'crear-carnes'),
    path('crear-panes/', form_panes, name = 'crear-panes'),
    path('crear-bebidas/', form_bebidas, name = 'crear-bebidas'),
    path('buscar/',buscar_productos, name='buscar-productos'),
    path('editar-carnes/<int:pk>/', actualizar_carne, name= 'editar-carnes'),
    path('borrar-carnes/<int:pk>/', borrar_carnes, name='borrar-carnes'),
    path('editar-bebidas/<int:pk>/', actualizar_bebidas, name='editar-bebidas'),
    path('borrar-bebidas/<int:pk>/', borrar_bebidas, name='borrar-bebidas'),
    path('editar-panes/<int:pk>/', actualizar_panes, name='editar-panes'),
    path('borrar-panes/<int:pk>/', borrar_panes, name='borrar-panes')
]
