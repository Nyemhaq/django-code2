from django.db import models

class CategoryModel(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 100, blank=True, null=True, unique=True)
    
    def __str__(self):
        return self.category
