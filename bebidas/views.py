from django.shortcuts import render
from bebidas.models import *
from random import randint

# Create your views here.

def bebidas(request):
    rand = randint(0, 2000)
    al1 = Bebidas.objects.create(name = 'Rutini', description = 'The mouthfeel combines ripe fruit with rich spices such as vanilla & chocolate imparted by oak. Great structure and smooth tannins, with a prolonged finish.', sku = rand, price = 2000, category = 'Malbec')
    context = {
        'bebida': al1
    }
    return render(request, 'bebidas.html', context=context)


def lista_bebidas(request):
    
    all = Bebidas.objects.all() 
     
    context ={
        'lista' : all
    }
    return render(request,'bebidas.html', context = context)
