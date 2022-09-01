from django.shortcuts import render, redirect
from contact.forms import Contact_form

def contact(request):
   data = {
      'form': Contact_form
   }
   if request.method == 'POST':
      form = Contact_form(data= request.POST)
      if form.is_valid():
         form.save()
      else:
         data['form'] = form
   return render(request, 'home_page.html', data)