from turtle import title
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField( max_length=50)
    decs = models.TextField()

    
