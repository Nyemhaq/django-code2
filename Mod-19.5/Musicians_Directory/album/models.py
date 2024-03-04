from django.db import models
from musician.models import createmusicianModel

class albumModel(models.Model):
    album_name = models.CharField(max_length = 100)
    musicianModel = models.ForeignKey(createmusicianModel, on_delete = models.CASCADE)
    album_release_date = models.DateField()
    rating = models.IntegerField()
    
    def __str__(self):
        return self.album_name
