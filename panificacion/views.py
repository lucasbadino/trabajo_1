from django.shortcuts import render, redirect
from random import randint
from panificacion.models import Panes
from panificacion.forms import Formulario_panes
from django.templatetags.static import static


def panes(request):
    rand = randint(0, 2000)
    al1 = Panes.objects.create(name = 'Pan Frances', description = 'baguette', sku = rand, price = 50)
    context = {
        'pan': al1
    }
    return render(request, 'panes/panes.html/', context=context)


def lista_panes(request):

    all = Panes.objects.all()

    context ={
        'lista' : all
    }
    return render(request,'panes/panes.html/', context = context)

def form_panes(request):
    if request.method == 'POST':
        form = Formulario_panes(request.POST)
        if form.is_valid():
            Panes.objects.create (
			     name = form.cleaned_data['name'],
			     price = form.cleaned_data['price' ],
                 description = form.cleaned_data['description'],
                 stock = form.cleaned_data['stock']
							)
        return redirect(lista_panes)
    elif request.method == 'GET':
        form = Formulario_panes
        context = {
            'form': form
        }
    return render(request, 'panes/crear_panes.html/', context=context)

def actualizar_panes(request, pk):
    if request.method == 'POST':
        form = Formulario_panes(request.POST)
        if form.is_valid():
            producto = Panes.objects.get(id=pk)
            producto.name = form.cleaned_data['name']
            producto.price = form.cleaned_data['price']
            producto.description = form.cleaned_data['description']
            producto.stock = form.cleaned_data['stock']
            producto.save()

            return redirect(lista_panes)

    elif request.method == 'GET':
        producto = Panes.objects.get(id=pk)

        form = Formulario_panes(initial={
            'name': producto.name,
            'price': producto.price,
            'description': producto.description,
            'stock': producto.stock})
        context = {'form': form}
        return render(request, 'panes/editar_panes.html/', context=context)


def borrar_panes(request, pk):
    if request.method == 'GET':
        producto = Panes.objects.get(pk=pk)
        context = {'producto': producto}
        return render(request, 'panes/borrar_panes.html', context=context)
    elif request.method == 'POST':
        producto = Panes.objects.get(pk=pk)
        producto.delete()
        return redirect(lista_panes)
