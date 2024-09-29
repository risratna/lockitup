# control/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lock/', views.lock_bike, name='lock_bike'),
    path('unlock/', views.unlock_bike, name='unlock_bike'),
]
