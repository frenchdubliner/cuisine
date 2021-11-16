from django.contrib import admin
from .models import User, UserProfile, Recipe, Ingredient, List_ingredients

# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(List_ingredients)