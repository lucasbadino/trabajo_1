from django.shortcuts import render
from random import randint
from panificacion.models import Panes


def panes(request):
    rand = randint(0, 2000)
    al1 = Panes.objects.create(name = 'Pan Frances', description = 'baguette', sku = rand, price = 50)
    context = {
        'pan': al1
    }
    return render(request, 'panes.html', context=context)


def lista_panes(request):
    
    all = Panes.objects.all() 
     
    context ={
        'lista' : all
    }
    return render(request,'panes.html', context = context)

