from django import forms

class Form_meats(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=200)
    stock = forms.IntegerField()
    price = forms.FloatField()
