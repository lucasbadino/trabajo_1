from django.urls import path
from users.views import login_request , register_request, user_profile, confirmation
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/', login_request, name='login'),
    path('register/', register_request, name='register'),
    path('logout/', LogoutView.as_view(template_name = 'user/logout.html'), name='logout'),
    path('user-profile/<int:pk>/',user_profile, name ='user_profile' ),
    path('confirmation/',confirmation ,name='confirmation')
]