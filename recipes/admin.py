from django.contrib import admin
from django.contrib.auth import get_user_model

# Register your models here.
from .models import Recipe, RecipeIngredient

User = get_user_model()

class RecipeIngredientsAdmin(admin.ModelAdmin):
    list_display = ['user', 'recipe', 'name', 'quantity', 'unit', 'description']
    read_only_fields = ['timestamp', 'updated']
    raw_id_fields = ['user']
    search_fields = ['title', 'description']

admin.site.register(RecipeIngredient, RecipeIngredientsAdmin)



class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'user']
    read_only_fields = ['timestamp', 'updated']
    raw_id_fields = ['user']
    search_fields = ['title', 'description']

admin.site.register(Recipe, RecipeAdmin)