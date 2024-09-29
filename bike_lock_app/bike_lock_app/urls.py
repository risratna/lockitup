"""
URL configuration for bike_lock_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls import include
from control.views import insert_number_view  # Import the new view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('control.urls')),  # API endpoints
    path('accounts/', include('django.contrib.auth.urls')),  # Login/Logout

    # path('map/', views.map_view, name='map'),  # map/ URL
    path('find-lock-number/', insert_number_view, name='find_lock_number'),
    path('insert-number/', insert_number_view, name='insert_number'),
    path('insure-bike/', insert_number_view, name='insure_bike'),
]