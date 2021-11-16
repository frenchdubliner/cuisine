from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=20)
    recipe_type = models.CharField(max_length=20)
    recipe_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.recipe_name}"

class List_ingredients(models.Model):
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)    
    ingredient = models.ForeignKey("Ingredient", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.quantity} {self.ingredient}"

class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.ingredient_name}"
