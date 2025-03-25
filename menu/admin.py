from django.contrib import admin
from .models import Menu, Item
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Menu)
class MenuAdmin(SummernoteModelAdmin):
    list_display = ('name', 'description', 'date_created', 'date_updated')
    list_filter = ('name', 'description', 'date_created', 'date_updated')
    search_fields = ('name', 'description', 'date_created', 'date_updated')

@admin.register(Item)
class ItemAdmin(SummernoteModelAdmin):
    list_display = ('name', 'description', 'item', 'price')
    list_filter = ('name', 'description', 'item', 'price')
    search_fields = ('name', 'description', 'item', 'price')


# Register your models here.
