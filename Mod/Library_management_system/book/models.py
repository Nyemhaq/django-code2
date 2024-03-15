from django.db import models
from category.models import CategoryModel

class BookModel(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    category = models.ForeignKey(CategoryModel, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='uploads/', null=True , blank = True)
    borrowing_price = models.CharField(max_length = 100)
    review = models.IntegerField(default = None, null=True, blank=True)
    
    def __str__(self):
        return self.title
