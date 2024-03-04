from django.db import models
from author.models import Author
class Profiles(models.Model):
    name = models.CharField(max_length = 100)
    about = models.TextField()
    # author = models.OneToOneField(Author, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.name

