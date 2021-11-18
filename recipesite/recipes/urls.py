from django.urls import path
from .views import (
    RecipeListView
)

app_name = "Recipes"

urlpatterns = [
    path('', RecipeListView.as_view(), name='Recipe-list'),
]