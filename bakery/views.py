from django.shortcuts import render, redirect
from random import randint
from product.models import Products
from product.forms import Form_product
from django.templatetags.static import static
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# this function was made to create the first products.
def bakeries(request):
    rand = randint(0, 2000)
    al1 = Products.objects.create(name = 'Pan Frances', description = 'baguette', sku = rand, price = 50)
    context = {
        'bakery': al1
    }
    return render(request, 'bakery/bakeries.html/', context=context)


def list_bakeries(request):
    all = Products.objects.all()
    context ={
        'list' : all
    }
    return render(request,'bakery/bakeries.html/', context = context)
@login_required
def create_bakeries(request):
    if request.method == 'POST':   
        form = Form_product(request.POST, request.FILES)
        if form.is_valid():
            Products.objects.create(
                    name = form.cleaned_data['name'],
                    price = form.cleaned_data['price'],
                    description = form.cleaned_data['description'],
                    stock = form.cleaned_data['stock'],
                    image = form.cleaned_data['image'],
                    category = 2
                )
        return redirect(list_bakeries)
      
        
    elif request.method == 'GET':
        if request.user.is_superuser:
            form = Form_product
            context = {
                'form': form
            }
        else:
            return redirect("login")
    return render(request, 'bakery/create_bakeries.html', context=context)

class Update_bakeries(LoginRequiredMixin, UpdateView):
    model = Products
    fields = ['name','description', 'price','image', 'category']
    template_name = 'bakery/edit_bakeries.html'
    success_url = '/all/'

         
@login_required
def delete_bakeries(request, pk):
    if request.method == 'GET':
        if request.user.is_superuser:
            product = Products.objects.get(pk=pk)
            context = {'product': product}
            return render(request, 'bakery/delete_bakeries.html', context=context)
        else:
            return redirect('login')
    elif request.method == 'POST':
        product = Products.objects.get(pk=pk)
        product.delete()
        return redirect(list_bakeries)

class Detail_bakeries(LoginRequiredMixin, DetailView):
    model = Products
    template_name = 'bakery/detail_bakeries.html'