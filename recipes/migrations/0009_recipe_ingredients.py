# Generated by Django 3.2.18 on 2023-03-12 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_auto_20230312_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(blank=True, null=True),
        ),
    ]