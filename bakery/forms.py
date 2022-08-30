from django import forms

class Form_bakeries(forms.Form):
    nombre = forms.CharField(max_length=50)
    descripcion = forms.CharField(max_length=200)
    stock = forms.IntegerField()
    precio = forms.FloatField()
    imagen = forms.ImageField(required=False)