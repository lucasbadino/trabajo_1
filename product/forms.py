from product.models import Products 
from django.forms import ModelForm



class Form_product(ModelForm):
    class Meta:
        model = Products
        fields = [ 'name', 'description', 'price', 'stock', 'image', 'category']

