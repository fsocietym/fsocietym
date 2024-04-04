from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=100)
    rollNo = models.IntegerField()
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()

class Car(models.Model):
    name = models.CharField(max_length=100)
    speed = models.IntegerField(default=60)
    
class RecipeModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    recipe_name = models.TextField(null=True)
    recipe_description = models.CharField(max_length=1500)
    recipe_file = models.FileField(upload_to='recipe_images')
    