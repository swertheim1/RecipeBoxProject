from django.shortcuts import render
from django.http import HttpResponse

from .models import Recipe

# Create your views here.

def recipe_list_view(request):

    recipes = Recipe.objects.all().order_by('timestamp')   
    return render(request, 'recipes/recipe_list_view.html', {'recipes':recipes} )


def recipe_detail_view(request, slug):
    # return HttpResponse(slug)
    recipe = Recipe.objects.get(slug=slug)
    directions = []
    
    print('recipe_directions', directions)
    for direction in directions:
        print('step before append', directions)
        directions.append(direction)
    print('afer append', directions)

    return render(request, 'recipes/recipe_detail_view.html', {'recipe':recipe, 'directions':directions } )