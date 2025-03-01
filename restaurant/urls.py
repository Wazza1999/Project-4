from django.contrib import admin
from django.urls import path
from menu import views as menu_views

urlpatterns = [
    path('menu/', menu_views.menu, name='menu'),
    path('admin/', admin.site.urls),
    ]
