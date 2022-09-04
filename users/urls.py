from django.urls import path
from users.views import login_request , register_request, user_profile, confirmation ,profile_complete, register_profile
from django.contrib.auth.views import LogoutView
from bakery.views import *
urlpatterns = [
    path('login/', login_request, name='login'),
    path('register/', register_request, name='register'),
    path('register-profile/', register_profile, name='register_profile'),
    path('logout/', LogoutView.as_view(template_name = 'user/logout.html'), name='logout'),
    path('user-profile/<int:pk>/',user_profile, name ='user_profile' ),
    path('confirmation/',confirmation ,name='confirmation'),
    path('user-complete/<int:pk>/', profile_complete, name='profile_complete'),
] 