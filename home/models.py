from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Department(models.Model):
    department = models.CharField(max_length=200)

    def __str__(self):
        return self.department
    
    class Meta:
        ordering = ['department']


class Student_UID(models.Model):
    uid = models.CharField(max_length=20)

    def __str__(self):
        return self.uid

    class Meta:
        ordering = ['id']
    


class student(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    student_UID = models.OneToOneField(Student_UID, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    address = models.TextField()

    def __str__(self):
        return self.name

    
    class Meta:
        ordering = ['id']
    

class Car(models.Model):
    name = models.CharField(max_length=100)
    speed = models.IntegerField(default=60)

    def __str__(self):
        return self.name
    
    
class RecipeModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    recipe_name = models.TextField(null=True)
    recipe_description = models.CharField(max_length=1500)
    recipe_file = models.FileField(upload_to='recipe_images')

    def __str__(self):
        return self.recipe_name
    
    