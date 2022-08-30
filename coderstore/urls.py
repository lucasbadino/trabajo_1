"""coderstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from coderstore.views import all_products, home_page, search_products, index
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('meat/', include('meat.urls')),
    path('drink/', include('drink.urls')),
    path('bakery/', include('bakery.urls')),
    path('search/',search_products, name='search-products'),
    path('inicio/', home_page, name='inicio'),
    path('user/', include('users.urls')),
    path('all/', all_products, name='all_products'),
    path('stock/', include('stock.urls')),
    path('cart/', include('cart.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)