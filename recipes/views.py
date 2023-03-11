from django.shortcuts import render               # get_list_or_404, redirect
from django.http import HttpResponse

# from django.contrib.auth.decorators import login_required
from .models import Recipe
# from .forms import RecipeForm


# Create your views here.


def recipe_list_view(request):
    recipes = Recipe.objects.all().order_by('timestamp')   
    return render(request, 'recipes/recipe_list_view.html', {'recipes':recipes} )


def recipe_detail_view(request, slug):
    recipe = Recipe.objects.get(slug=slug)

    return render(request, 'recipes/recipe_detail_view.html', {'recipe':recipe } )


def recipe_create_view(request):
    return render(request, 'recipes/recipe_create_view.html')





