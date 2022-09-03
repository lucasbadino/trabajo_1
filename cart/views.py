from django.shortcuts import render, redirect
from cart.cart import Cart
from product.models import Products
from django.contrib.auth.decorators import login_required


def add_product(request,product_id):
    cart=Cart(request)
    product=Products.objects.get(id=product_id)
    cart.add(product)
    return redirect ("test")
  
  
def delete_product(request, product_id):
    cart = Cart(request)
    product=Products.objects.get(id=product_id)
    cart.delete(product)
    return redirect("test")


def subtract_product(request, product_id):
    cart = Cart(request)
    product=Products.objects.get(id=product_id)
    cart.subtract(product)
    return redirect("test")

def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect("test")


def test(request):
    return render(request, "prueba.html")

@login_required
def checkout(request):
    total = 0
    if "cart" in request.session.keys():
            for key, value in request.session["cart"].items():
                total += int(value["amount"])
                context = {
                    'product' : total
                }
    return render(request, "cart/checkout.html" , context=context)
    

