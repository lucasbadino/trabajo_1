from django.urls import path
from meat.views import  meats, list_of_meats, edit_meats, delete_meats, form_meats




urlpatterns = [
    path('meats/', list_of_meats, name='meats'),
    path('create-meats/', form_meats, name = 'create_meats'),
    path('edit-meats/<int:pk>/', edit_meats, name= 'edit_meats'),
    path('delete-meats/<int:pk>/', delete_meats, name='delete_meats'),
]
