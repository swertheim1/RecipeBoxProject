from django.shortcuts import render

from .models import Recipe

# Create your views here.

def recipe_list_view(request):

    # query_dict = request.GET

    # try: 
    #     query = int(query_dict.get('q'))
    # except:
    #     query = None
    # recipe_obj = None

    # if query is not None:
    #     recipe_obj = Recipe.objects.get(id=query)

    recipes = Recipe.objects.all().order_by('date')   
    # context = {
    #     'recipes': recipes
    # }
   

    return render(request, 'recipes/recipe_list_view.html', {'recipes':recipes} )