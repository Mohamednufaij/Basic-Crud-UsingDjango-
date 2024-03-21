from django.db import models
from django import forms
# Create your models here.
class Regmodel(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    country=models.CharField(max_length=200,default=None)
    