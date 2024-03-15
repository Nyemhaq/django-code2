from django.db import models
from django.contrib.auth.models import User

class BookModel(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/', null=True , blank = True)
    borrowing_price = models.CharField(max_length = 100)
    review = models.IntegerField(default = None, null=True, blank=True)
    
    def __str__(self):
        return self.title