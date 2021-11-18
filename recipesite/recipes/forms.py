from django import forms
from .models import Recipe


class RecipeModelForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            'recipe_name ',
            'recipe_type ',
            'recipe_date ',
        )
