from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Recipe, RecipeIngredient
# Create your tests here.

User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('sam', password='test1234')

    def test_user_pw(self):
        checked = self.user_a.check_password('test1234')
        self.assertTrue(checked)


class RecipeTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('susan', password='test1234')
        self.recipe_a = Recipe.objects.create(
            user = 'self.user_a',
            title = 'Smoked Salmon'
            # description = 'test description'
        )
        print(self.user_a)
        self.user_b = User.objects.create_user('sam', password='test1234')

    def test_user_count(self):
        qs = User.objects.all()
        self.assertEqual(qs.count(), 2)

    def test_user_recipe_count(self):
        user_a = self.user_a
        user_b = self.user_b
        qs_a = user_a.recipe_set.all()
        qs_b = user_b.recipe_set.all()
        self.assertEqual(qs_a.count(), 0)
        self.assertEqual(qs_b.count(), 0)

    def test_user_recipe_count(self):
        user_a = self.user_a
        user_b = self.user_b
        qs_a = user_a.recipe_set.all()
        qs_b = user_b.recipe_set.all()
        self.assertEqual(qs_a.count(), 1)
        self.assertEqual(qs_b.count(), 0)