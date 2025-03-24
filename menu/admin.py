from django.contrib import admin
from .models import Menu, Item
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Menu)
class MenuAdmin(SummernoteModelAdmin):
    name

# Register your models here.
admin.site.register(Item)
