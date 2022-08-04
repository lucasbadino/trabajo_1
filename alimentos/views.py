from django.shortcuts import render
from alimentos.models import *
from random import randint

# Create your views here.

def alimentos(request):
    rand = randint(0, 2000)
    al1 = Productos.objects.create(name = 'Carne', description = 'Carne de ternera', sku = rand, price = 2000)
    context = {
        'carne': al1
    }
    return render(request, 'alimentos.html', context=context)


def lista_alimentos(request):
    
    all = Productos.objects.all() 
     
    context ={
        'lista' : all
    }
    return render(request,'alimentos.html', context = context)



