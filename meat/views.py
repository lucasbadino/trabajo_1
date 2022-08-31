from django.shortcuts import render, redirect
from meat.models import *
from random import randint
from django.templatetags.static import static
from meat.forms import Form_meats
from django.views.generic import DetailView,UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


# this function was made to create the first products.
def meats(request):
    rand = randint(0, 2000)
    al1 = Products.objects.create(name = 'Carne', description = 'Carne de ternera', sku = rand, price = 2000)
    context = {
        'meat': al1
    }
    return render(request, 'meat/meats.html', context=context)


def list_of_meats(request):

    all = Products.objects.all()

    context ={
        'list' : all
    }
    return render(request,'meat/meats.html', context = context)


@login_required
def create_meats(request):
    if request.method == 'POST':
        form = Form_meats(request.POST, request.FILES)
        if form.is_valid():
            Products.objects.create (
			     name = form.cleaned_data['nombre'],
			     price = form.cleaned_data['precio' ],
                 description = form.cleaned_data['descripcion'],
                 stock = form.cleaned_data['stock'],
                 image = form.cleaned_data['imagen'],
							)
        return redirect(list_of_meats)
    elif request.method == 'GET':
        if request.user.is_superuser:
            form = Form_meats
            context = {
                'form': form
            }
        else:
            return redirect("login")
    return render(request, 'meat/create_meats.html', context=context)

class Update_meats(LoginRequiredMixin, UpdateView):
    model = Products
    fields = ['name','description', 'sku', 'price','image']
    template_name = 'meat/edit_meats.html'
    success_url = '/all/'
# @login_required
# def edit_meats(request, pk):
#     if request.method == 'POST':
#         form = Form_meats(request.POST, request.FILES)
#         if form.is_valid():
#             product = Products.objects.get(id=pk)
#             product.name = form.cleaned_data['nombre']
#             product.price = form.cleaned_data['precio']
#             product.description = form.cleaned_data['descripcion']
#             product.stock = form.cleaned_data['stock']
#             product.image = form.cleaned_data['imagen']
#             product.save()

#             return redirect(list_of_meats)

#     elif request.method == 'GET':
#         if request.user.is_superuser:
#             product = Products.objects.get(id=pk)

#             form = Form_meats (initial={
#                 'nombre': product.name,
#                 'precio': product.price,
#                 'descripcion': product.description,
#                 'stock': product.stock,
#                 'imagen': product.image,
#                 })
#             context = {'form': form}
#             return render(request, 'meat/edit_meats.html', context=context)
#         else:
#             return redirect("login")
    




@login_required
def delete_meats(request, pk):
    if request.method == 'GET':
        if request.user.is_superuser:
            product = Products.objects.get(pk=pk)
            context = {'product': product}
            return render(request, 'meat/delete_meats.html', context=context)
        else:
            return redirect("login")
    elif request.method == 'POST':
        product = Products.objects.get(pk=pk)
        product.delete()
        return redirect(list_of_meats)
class Detail_Products(LoginRequiredMixin, DetailView):
    model = Products
    template_name = 'meat/detail_meats.html'