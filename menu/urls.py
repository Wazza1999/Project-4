from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('menu/', views.menu_view, name='menu')
]