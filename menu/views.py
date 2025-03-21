from django.shortcuts import render
from django.views import generic
from .models import Menu

# Create your views here.

def menu_view(request):
    menus = Menu.objects.prefetch_related('items').all()
    return render(request, 'menu/menu_list.html', {'menus': menus})
