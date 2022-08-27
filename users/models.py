import email
from email.mime import image
from pyexpat import model
from django.db import models

# Create your models here.
class User_profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile')#restrict(no deja borrar el usuario) 
    email = models.EmailField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='profile_image/', blank=True, null=True)
    

    def __str__(self):
        return self.user.username +'- user profile'