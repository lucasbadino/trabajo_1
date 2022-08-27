from django.urls import path
from users.views import login_request , register_request, user_profile, confirmation ,profile_complete
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings
from bakery.views import *
urlpatterns = [
    path('login/', login_request, name='login'),
    path('register/', register_request, name='register'),
    path('logout/', LogoutView.as_view(template_name = 'user/logout.html'), name='logout'),
    path('user-profile/<int:pk>/',user_profile, name ='user_profile' ),
    path('confirmation/',confirmation ,name='confirmation'),
    path('user-complete/<int:pk>/', profile_complete, name='profile_complete'),
] 