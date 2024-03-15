from django.db import models
from category.models import CategoryModel
from django.contrib.auth.models import User

class BookModel(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    category = models.ForeignKey(CategoryModel, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='uploads/', null=True , blank = True)
    borrowing_price = models.IntegerField()
    total_copy = models.IntegerField(default = None, null=True, blank=True)
    review = models.TextField(null=True, blank=True)
    borrow_by = models.ManyToManyField(User,related_name='purchased_books', null=True, blank=True)
    borrow_date = models.DateTimeField(auto_now_add=True, null=True, blank=True) 
    returned = models.BooleanField(default=False,null=True, blank=True)
    
    def __str__(self):
        return self.title
