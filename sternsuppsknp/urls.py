"""sternsuppsknp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView

from .views import home_page,about_page,contact_page,login_page,register_page

urlpatterns = [
    path(r'',home_page, name='home'),
    path(r'about/',about_page, name='about'),
    path(r'contact/',contact_page, name='contact'),
    path(r'login/',login_page, name='login'),
    path(r'cart/',include("carts.urls", namespace='cart')),
    path(r'register/',register_page,name='register'),
    path(r'bootstrap/',TemplateView.as_view(template_name='bootstrap/example.html')),
    path(r'products/',include("products.urls", namespace='products')),
    path(r'search/',include("search.urls", namespace='search')),
    path(r'admin/', admin.site.urls),
]

if settings.DEBUG:
	urlpattern = urlpatterns + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpattern = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)