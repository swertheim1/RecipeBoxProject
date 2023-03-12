from django.contrib import admin

from .models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'user']
    read_only_fields = ['timestamp', 'updated']
    raw_id_fields = ['user']
    search_fields = ['title', 'description']

admin.site.register(Recipe, RecipeAdmin)