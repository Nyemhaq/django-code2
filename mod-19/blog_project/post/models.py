from django.db import models
from category.models import Category
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='uploads/',blank=True, null=True)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'comment')
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"Commented By {self.name}"
        