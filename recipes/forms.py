from django import forms

from .models import Recipe, RecipeIngredient


class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'directions', 'slug', 'thumb']


class CreateIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['recipe', 'name', 'quantity', 'unit']