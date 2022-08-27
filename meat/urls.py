from django.urls import path
from meat.views import  meats, list_of_meats, edit_meats, delete_meats, create_meats , Detail_Products




urlpatterns = [
    path('meats/', list_of_meats, name='meats'),
    path('create-meats/', create_meats, name = 'create_meats'),
    path('edit-meats/<int:pk>/', edit_meats, name= 'edit_meats'),
    path('delete-meats/<int:pk>/', delete_meats, name='delete_meats'),
    path('detail-meats/<int:pk>/', Detail_Products.as_view(), name='detail-meats'),
]
