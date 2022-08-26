from django.views.generic import DetailView, UpdateView
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from drink.models import  *
from random import randint
from drink.forms import Form_drinks
from django.templatetags.static import static
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# this function was made to create the first products.
def drinks(request):
    rand = randint(0, 2000)
    al1 = Drinks.objects.create(name = 'Rutini', description = 'The mouthfeel combines ripe fruit with rich spices such as vanilla & chocolate imparted by oak. Great structure and smooth tannins, with a prolonged finish.', sku = rand, price = 2000, category = 'Malbec')
    context = {
        'drink': al1
    }
    return render(request, 'drink/drinks.html', context=context)


def list_drinks(request):

    all = Drinks.objects.all()

    context ={
        'list' : all
    }
    return render(request,'drink/drinks.html', context = context)

@login_required
def create_drinks(request):
    if request.method == 'POST':
        form = Form_drinks(request.POST, request.FILES)
        if form.is_valid():
            Drinks.objects.create (
			     name = form.cleaned_data['name'],
			     price = form.cleaned_data['price' ],
                 description = form.cleaned_data['description'],
                 stock = form.cleaned_data['stock'],
                 image = form.cleaned_data['image'],
							)
        return redirect(list_drinks)
    elif request.method == 'GET':
        if request.user.is_superuser:
            form = Form_drinks
            context = {
                'form': form
            }
            return render(request, 'drink/create_drinks.html', context=context)
        else:
            return redirect("login")
    

@login_required
def edit_drinks(request, pk):
    if request.method == 'POST':
        form = Form_drinks(request.POST, request.FILES)
        if form.is_valid():
            product = Drinks.objects.get(id=pk)
            product.name = form.cleaned_data['name']
            product.price = form.cleaned_data['price']
            product.description = form.cleaned_data['description']
            product.stock = form.cleaned_data['stock']
            product.image = form.cleaned_data['image']
            product.save()

            return redirect(list_drinks)

    elif request.method == 'GET':
        if request.user.is_superuser:
            product = Drinks.objects.get(id=pk)

            form = Form_drinks(initial={
                'name': product.name,
                'price': product.price,
                'description': product.description,
                'stock': product.stock,
                'image': product.image})
            context = {'form': form}
            return render(request, 'drink/edit_drinks.html', context=context)
        else:
            return redirect("login")

@login_required
def delete_drinks(request, pk):
    if request.method == 'GET':
        if request.user.is_superuser:
            product = Drinks.objects.get(pk=pk)
            context = {'product': product}
            return render(request, 'drink/delete_drinks.html', context=context)
        else:
            return redirect("login")
    elif request.method == 'POST':
        product = Drinks.objects.get(pk=pk)
        product.delete()
        return redirect(list_drinks)

class Detail_drinks(LoginRequiredMixin , DetailView):
    model = Drinks
    template_name = 'drink/detail_drinks.html'

