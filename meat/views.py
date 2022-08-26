from django.shortcuts import render, redirect
from meat.models import *
from random import randint
from django.templatetags.static import static
from meat.forms import Form_meats
from django.views.generic import DetailView
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
			     name = form.cleaned_data['name'],
			     price = form.cleaned_data['price' ],
                 description = form.cleaned_data['description'],
                 stock = form.cleaned_data['stock'],
                 image = form.cleaned_data['image'],
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

@login_required
def edit_meats(request, pk):
    if request.method == 'POST':
        form = Form_meats(request.POST, request.FILES)
        if form.is_valid():
            product = Products.objects.get(id=pk)
            product.name = form.cleaned_data['name']
            product.price = form.cleaned_data['price']
            product.description = form.cleaned_data['description']
            product.stock = form.cleaned_data['stock']
            product.image = form.cleaned_data['image']
            product.save()

            return redirect(list_of_meats)

    elif request.method == 'GET':
        if request.user.is_superuser:
            product = Products.objects.get(id=pk)

            form = Form_meats (initial={
                'name': product.name,
                'price': product.price,
                'description': product.description,
                'stock': product.stock,
                'image': product.image,
                })
            context = {'form': form}
            return render(request, 'meat/edit_meats.html', context=context)
        else:
            return redirect("login")
    




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