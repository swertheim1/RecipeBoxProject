from django.conf import settings
from django.db import models
from django.utils.text import slugify
from .validators import validate_unit_of_measure

# Create your models here.
class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='1',)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True, null=True)
    ingredients = models.TextField(blank=True, null=True,)
    directions = models.TextField(blank=True, null=True,)
    timestamp = models.DateTimeField(auto_now_add=True) # automatically input time when record is created
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField()
    thumb = models.ImageField(default='default.png', blank=True)
    

    
    
    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.description[:50] + '...'
    

# class RecipeIngredient(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='1',)
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
#     name = models.CharField(max_length=220)
#     quantity = models.FloatField(max_length=20)
#     unit = models.CharField(max_length=20, validators=[validate_unit_of_measure])
#     description = models.TextField(blank=True, null=True, max_length=255)
#     directions = models.TextField(blank=True, null=True, max_length=255)
#     timestamp = models.DateTimeField(auto_now_add=True) # automatically input time when record is created
#     updated = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name
    

# class RecipeImage():
#     recipe = models.ForeignKey(Recipe)

