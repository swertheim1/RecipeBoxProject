from django.shortcuts import render, redirect               # get_list_or_404,
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from .models import Recipe
from . import forms

from .forms import CreateRecipeForm


# Create your views here.


def recipe_list_view(request):
    """
    View to display list of all recipes - will have to be limited in size eventaully 
    or paginated - don't know how to do that yet
    
    """
    recipes = Recipe.objects.all().order_by('title')   
    return render(request, 'recipes/recipe_list_view.html', {'recipes':recipes} )


def recipe_detail_view(request, slug):
    """
    View to display individual recipe based on the slug value
    
    """
    recipe = Recipe.objects.get(slug=slug)
    
    return render(request, 'recipes/recipe_detail_view.html', {'recipe':recipe } )


def recipe_search_view(request):
    """
    Function to search the database for recipes
    
    """

    # if search was made 
    print(request.method == "POST") 
    if request.method == "POST":
        
        query_name = request.POST.get('title', None)
        print(query_name)
        
        if query_name:
            recipes = Recipe.objects.filter(title__contains=query_name)
            print(recipes)
            return render(request, 'recipes/recipe_search_view.html', {'recipes':recipes})
        else:
            recipes = Recipe.objects.all().order_by('timestamp')
            return render(request, 'recipes/recipe_list_view.html', {'recipes':recipes})
    else:
        
        return render(request, 'recipes/recipe_search_view.html')


@login_required(login_url="/accounts/login/")
def recipe_create_view(request):
    """
    Function that is used to save a new recipe to the database
    Log is required for this 
    """
    if request.method == "POST":
        form = CreateRecipeForm(request.POST, request.FILES)
        if form.is_valid():
             form.save()

        return redirect('recipes:list')
    else:
        form = CreateRecipeForm()
    return render(request, 'recipes/recipe_create_view.html', {'form': form})





