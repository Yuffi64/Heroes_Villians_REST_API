from pyexpat import model
from django.db import models

# Create your models here.

class super_type(models.Model):
    type = models.CharField(max_length=300)