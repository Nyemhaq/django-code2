from django.db import models

class createmusicianModel (models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 20)
    instrument_type = models.TextField()
    
    def __str__(self):
        return self.first_name


