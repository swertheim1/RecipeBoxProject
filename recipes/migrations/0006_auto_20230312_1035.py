# Generated by Django 3.2.18 on 2023-03-12 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_recipe_thumb'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='quantity',
            field=models.FloatField(max_length=20),
        ),
    ]
