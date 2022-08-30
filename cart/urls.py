from django.urls import path
from cart.views import *

urlpatterns = [
    path("test/", test, name="test"),
    path("add/<int:product_id>/", add_product, name="Add"), 
    path("delete/<int:product_id>/", delete_product, name="Delete"),
    path("subtract/<int:product_id>/", subtract_product, name="Sub"), 
    path("clear/", clear_cart, name="Clear"),

]
