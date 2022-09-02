from django.shortcuts import render, redirect, get_object_or_404
from meat.models import Products
from bakery.models import Bakeries
from drink.models import Drinks
from cart.cart import Cart
# Create your views here.





def add_product(request, product_id):
    cart = Cart(request)
    try: 
        product1 = get_object_or_404(Products, id= product_id)
        
    except:
        try:
            product1 = get_object_or_404(Drinks, id= product_id) 
        except:
            product1 = get_object_or_404(Bakeries, id= product_id)
    
    cart.add(product1)
    return redirect("test")    

def delete_product(request, product_id):
    cart = Cart(request)
    try: 
        product1 = get_object_or_404(Products, id= product_id)
        
    except:
        try:
            product1 = get_object_or_404(Drinks, id= product_id) 
        except:
            product1 = get_object_or_404(Bakeries, id= product_id)
    cart.delete(product1)
    return redirect("test")


def subtract_product(request, product_id):
    cart = Cart(request)
    try: 
        product1 = get_object_or_404(Products, id= product_id)
        
    except:
        try:
            product1 = get_object_or_404(Drinks, id= product_id) 
        except:
            product1 = get_object_or_404(Bakeries, id= product_id)
    cart.subtract(product1)
    return redirect("test")

def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect("test")


def test(request):
    return render(request, "prueba.html")

def checkout(request):
    total = 0
    if request.user.is_authenticated:
        if "cart" in request.session.keys():
            for key, value in request.session["cart"].items():
                total += int(value["amount"])
                context = {
                    'product' : total
                }
    return render(request, "cart/checkout.html" , context=context)
    

# def add_product(request,pk):
#     cart=Cart(request)
#     product=Product.objects.get(id=pk)
#     cart.add(product=product)
#     return redirect ('/Productos/Shop_single/%d/?valido'%pk)