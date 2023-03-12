from django.forms import ModelForm
from django import forms
from .models import Recipe


class CreateRecipeForm(ModelForm):
    title = forms.CharField()
    description = forms.CharField()
    ingredients = forms.Textarea()
    directions = forms.Textarea()
    slug = forms.CharField()
    thumb = forms.ImageField()

    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'directions', 'slug', 'thumb']


