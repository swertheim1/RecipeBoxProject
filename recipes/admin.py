from django.contrib import admin
from django.contrib.auth import get_user_model

# Register your models here.
from .models import Recipe, RecipeIngredient

User = get_user_model()

admin.site.register(RecipeIngredient)



class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'user']
    read_only_fields = ['timestamp', 'updated']
    raw_id_fields = ['user']
    search_fields = ['title', 'description']

admin.site.register(Recipe, RecipeAdmin)