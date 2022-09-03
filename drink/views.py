
from django.views.generic import DetailView, UpdateView
from django.shortcuts import render, redirect
from product.models import  *
from random import randint
from product.forms import Form_product
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from product.models import Products

# this function was made to create the first products.
def drinks(request):
    rand = randint(0, 2000)
    al1 = Products.objects.create(name = 'Rutini', description = 'The mouthfeel combines ripe fruit with rich spices such as vanilla & chocolate imparted by oak. Great structure and smooth tannins, with a prolonged finish.', sku = rand, price = 2000, category = 'Malbec')
    context = {
        'drink': al1
    }
    return render(request, 'drink/drinks.html', context=context)


def list_drinks(request):

    all = Products.objects.all()

    context ={
        'list' : all
    }
    return render(request,'drink/drinks.html', context = context)

@login_required
def create_drinks(request):
    if request.method == 'POST':
        form = Form_product(request.POST, request.FILES)
        if form.is_valid():
            Products.objects.create(
                    name = form.cleaned_data['name'],
                    price = form.cleaned_data['price'],
                    description = form.cleaned_data['description'],
                    stock = form.cleaned_data['stock'],
                    image = form.cleaned_data['image'],
                    category = 3
                )
        return redirect(list_drinks)
      
    elif request.method == 'GET':
        if request.user.is_superuser:
            form = Form_product
            context = {
                'form': form
            }
            return render(request, 'drink/create_drinks.html', context=context)
        else:
            return redirect("login")

class Update_drinks(LoginRequiredMixin, UpdateView):
    model = Products
    fields = ['name','description', 'price','image','category']
    template_name = 'drink/edit_drinks.html'
    success_url = '/all/'

@login_required
def delete_drinks(request, pk):
    if request.method == 'GET':
        if request.user.is_superuser:
            product = Products.objects.get(pk=pk)
            context = {'product': product}
            return render(request, 'drink/delete_drinks.html', context=context)
        else:
            return redirect("login")
    elif request.method == 'POST':
        product = Products.objects.get(pk=pk)
        product.delete()
        return redirect(list_drinks)

class Detail_drinks(LoginRequiredMixin , DetailView):
    model = Products
    template_name = 'drink/detail_drinks.html'

