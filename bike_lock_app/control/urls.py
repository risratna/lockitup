# control/urls.py
from django.urls import path
from . import views
from .views import insert_number_view  # Import the new view

urlpatterns = [
    # path('insert-number/', insert_number, name='insert_number'),
    path('', views.home, name='home'),
    path('lock/', views.lock_bike, name='lock_bike'),
    path('unlock/', views.unlock_bike, name='unlock_bike'),
    path('login/', views.loginPage, name='loginPage'),
    path('login/locka1/', views.lockPage, name='lockPage'),
    path('map/', views.map, name='map')
]

