from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Category(models.Model):
    name = models.Charfield(max_length=100)
    description = models.TextField(blank=True)
