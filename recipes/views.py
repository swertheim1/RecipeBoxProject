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
    
    # directions = []
    # print('recipe_directions', directions)
    # for direction in  recipe.directions:
    #     print('step before append', directions)
    #     directions.append(direction)
    # print('afer append', directions)

    return render(request, 'recipes/recipe_detail_view.html', {'recipe':recipe } )




# def recipe_detail_view(request, slug):
#     recipe = Recipe.objects.get(slug=slug)  

#     return render(request, 'recipes/recipe_detail_view.html', {'recipe': recipe} )


# # @login_required
# def recipe_create_view(request):
#     form = RecipeForm(request.POST or None)
#     context = {
#        'form': form
#     }
#     # form = RecipeForm(request.POST or None)
#     return render(request, 'recipes/create_update_view.html', context)


# # @login_required
# def recipe_update_view(request, id=None):
#     context = {
       
    # }
    # form = RecipeForm(request.POST or None)
    # return render(request, 'recipes/create_update_view.html', context)





