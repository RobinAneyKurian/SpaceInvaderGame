from distutils.command.upload import upload
from django.db import models
from django.forms import CharField, ImageField

# Create your models here.

class Destination(models.Model):
     
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    desc = models.TextField()
    proplayer = models.BooleanField(default=False)
    img = models.ImageField(upload_to="pics")

