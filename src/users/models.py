from django.db import models

from django import forms

# Create your models here.
class User(models.Model):
	username	= models.CharField(max_length=20, blank=False, null=False)
	password	= models.CharField(max_length=20, blank=False, null=False) 
	email		= models.EmailField(max_length=254, blank=False, null=False)
	first_name	= models.CharField(max_length=20, blank=False, null=False)
	last_name	= models.CharField(max_length=20, blank=False, null=False)