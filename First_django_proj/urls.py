"""
URL configuration for First_django_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path

from home.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # path('', home, name='Home'),
    # path('about/', about, name='About'),
    # path('contact/', contact, name='Contact'),
    path('', explore_recipe, name='bestrecipes'),

    path('add_recipes/', recipes, name='recipes'),
    path('update_recipe/<id>', update_recipe, name='update_recipe'),
    path('delete_recipe/<id>', delete_recipe, name='delete_recipe'),

    path('login/', login_page, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_page, name='logout'),


    path('my_recipe/', my_recipe, name='my_recipe'),


    path('admin/', admin.site.urls),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
