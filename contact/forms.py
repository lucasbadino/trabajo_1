from django import forms
from contact.models import Contact
class Contact_form(forms.ModelForm):

    class Meta:
        model = Contact 
        fields =['nombre','email', 'telefono', 'tipo_de_consulta', 'comentario', 'notificaciones'] 
        
