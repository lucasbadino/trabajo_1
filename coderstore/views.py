from django.shortcuts import render
from alimentos.models import Productos
from bebidas.models import Bebidas
from panificacion.models import Panes

def inicio(request):
    return render(request, "inicio.html", context={})


def buscar_productos(request):
    search = request.GET['search']
    carne = Productos.object.filter(name__icontains = search)
    bebida = Bebidas.object.filter(name__icontains = search)
    panes = Panes.object.filter(name__icontains = search)
    context = {	
        'carnes': carne,
        'bebidas': bebida,
        'panes': panes
                }
    return render(request, 'search_product.html', context = context)

