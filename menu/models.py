from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Menu(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add= True)
    date_updated = models.DateTimeField(auto_now= True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Item(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    item = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    def __str__(self):
        return f"{self.name} (£{self.price})"