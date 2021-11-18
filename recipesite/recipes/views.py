from django.shortcuts import render
from django.views import generic
from .models import Recipe

# Create your views here.

class RecipeListView(generic.ListView):
    template_name = "recipe_list.html"
    queryset = Recipe.objects.all()
    context_object_name = "recipes"
