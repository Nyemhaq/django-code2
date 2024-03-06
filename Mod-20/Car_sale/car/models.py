from django.db import models
from brand.models import Brand
from django.contrib.auth.models import User

class Car(models.Model):
    name = models.CharField(max_length = 100)
    details = models.TextField()
    price = models.CharField(max_length = 50)
    image = models.ImageField(upload_to='uploads/' ,blank=True, null=True)
    total_car = models.IntegerField()
    Brand = models.ForeignKey(Brand, on_delete = models.CASCADE)
    buy = models.BooleanField(default = None)
    
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    post = models.ForeignKey(Car, on_delete = models.CASCADE, related_name = 'comment')
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"Commented By {self.name}"

    

class UserBuyCar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    car = models.ManyToManyField(Car)

    def __str__(self):
        return self.user.first_name