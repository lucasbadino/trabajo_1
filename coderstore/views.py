from django.shortcuts import render
from alimentos.models import Productos
from bebidas.models import Bebidas
from panificacion.models import Panes

def inicio(request):
    return render(request, "inicio.html", context={})


def buscar_productos(request):
   search = request.GET['search']
   carne = Productos.objects.filter(name__icontains = search)
   bebida = Bebidas.objects.filter(name__icontains = search)
   panes = Panes.objects.filter(name__icontains = search)
   dic = carne.union(bebida, panes)
   context = {	
       'carne': dic
                     }
   return render(request, 'search_product.html', context = context)

