from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    ingredients = models.TextField(default='')
    steps = models.TextField(default='')
    date = models.DateTimeField(auto_now_add=True) # automatically input time when record is created
    slug = models.SlugField()
    # add thumbnails
    # add author

    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.description[:50] + '...'
