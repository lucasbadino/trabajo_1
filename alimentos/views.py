from contextvars import Context
from importlib.resources import contents
from django.shortcuts import render, redirect
from alimentos.models import *
from random import randint
from django.templatetags.static import static 
from alimentos.forms import Formulario_carnes
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

def form_carne(request):
    if request.method == 'POST':
        form = Formulario_carnes(request.POST)
        if form.is_valid():
            Productos.objects.create (
			     name = form.cleaned_data['name'],
			     price = form.cleaned_data['price' ],
                 description = form.cleaned_data['description'],
                 stock = form.cleaned_data['stock']
							)
        return redirect(lista_alimentos)
    elif request.method == 'GET':
        form = Formulario_carnes
        context = {
            'form': form
        }
    return render(request, 'crear_carnes.html', context=context)



