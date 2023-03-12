from django.test import TestCase
from .models import Recipe

from .models import Recipe
from django.contrib.auth.models import User
# Create your tests here.

class RecipeTestCase(TestCase):
    def setUp(self):
        self.number_of_recipes = 500
        user1 = User.objects.create_user('Mary',"", 'test1234' )
        user1.save()
        user1.is_staff = True
        user1.save()
        for i in range(0, self.number_of_recipes):

            Recipe.objects.create(title='Recipe',
                                description = 'recipe description',
                                directions = 'recipe direction 1\n recipe direction 2',
                                ingredients = 'recipe ingredent 1',
                                slug = 'recipe',
        )
        
    def test_recipe_queryset_exists(self):
        # test there are recipe objects in the database
        qs = Recipe.objects.all()
        self.assertTrue(qs.exists)

    def test_queryset_count(self):
        qs = Recipe.objects.all()
        self.assertEqual(qs.count(), self.number_of_recipes)

    def test_recipe_delete(self):
        self.number_of_deletions = 50

        Recipe.objects.filter(id__in=list(Recipe.objects.values_list('pk', flat=True)[:self.number_of_deletions])).delete()
        
        qs = Recipe.objects.all()
        self.assertEqual(qs.count(), self.number_of_recipes - self.number_of_deletions)
    
# class RecipeIngredientTestCase(TestCase):
#     def setUp(self):
#         self.number_of_ingredients = 10
#         user1 = User.objects.create_user('Mary',"", 'test1234' )
#         user1.save()
#         recipe = Recipe.objects.create(
#             title='Recipe',
#             description = 'recipe description',
#             directions = 'recipe direction 1\n recipe direction 2',
#         )

#         for i in range(0, self.number_of_ingredients):
#             RecipeIngredient.objects.create(
#                 recipe_id = 1,
#                 name ='ingredient',
#                 quantity = 5,
#                 unit = 'cups',
#                 directions = 'this a direction'
#         )
        
#     def test_recipe_queryset_exists(self):
#         # test there are recipe objects in the database
#         qs = RecipeIngredient.objects.all()
#         self.assertTrue(qs.exists)

#     def test_queryset_count(self):
#         qs = RecipeIngredient.objects.all()
#         self.assertEqual(qs.count(), self.number_of_ingredients)

#     def test_recipe_delete(self):
#         self.number_of_deletions = 3

        RecipeIngredient.objects.filter(id__in=list(RecipeIngredient.objects.values_list('pk', flat=True)[:self.number_of_deletions])).delete()
        
        qs = RecipeIngredient.objects.all()
        self.assertEqual(qs.count(), self.number_of_ingredients - self.number_of_deletions)
    