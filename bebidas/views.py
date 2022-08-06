from django.shortcuts import render, redirect
from bebidas.models import *
from random import randint
from bebidas.forms import Formulario_bebidas
from django.templatetags.static import static

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

def form_bebidas(request):
    if request.method == 'POST':
        form = Formulario_bebidas(request.POST)
        if form.is_valid():
            Bebidas.objects.create (
			     name = form.cleaned_data['name'],
			     price = form.cleaned_data['price' ],
                 description = form.cleaned_data['description'],
                 stock = form.cleaned_data['stock']
							)
        return redirect(lista_bebidas)
    elif request.method == 'GET':
        form = Formulario_bebidas
        context = {
            'form': form
        }
    return render(request, 'crear_bebidas.html', context=context)