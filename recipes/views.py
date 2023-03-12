from django.shortcuts import render, redirect               # get_list_or_404,
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from .models import Recipe
from . import forms

from .forms import CreateRecipeForm


# Create your views here.


def recipe_list_view(request):
    recipes = Recipe.objects.all().order_by('title')   
    return render(request, 'recipes/recipe_list_view.html', {'recipes':recipes} )


def recipe_detail_view(request, slug):
    recipe = Recipe.objects.get(slug=slug)
    
    return render(request, 'recipes/recipe_detail_view.html', {'recipe':recipe } )


def recipe_search_view(request):
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
    if request.POST:
        form = CreateRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home')
    return render(request, 'recipes/recipe_create_view.html', {'form': form})





