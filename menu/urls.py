from . import views
from django.urls import path

urlpatterns = [
    path('menu/', views.menu_view, name='menu'),
]