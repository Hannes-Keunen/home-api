from django.db import models

# Create your models here.

class Device(models.Model):
    address = models.CharField(max_length=5)
