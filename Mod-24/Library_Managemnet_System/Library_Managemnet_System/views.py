from django.shortcuts import render
from category.models import CategoryModel 
from book.models import BookModel

def home(req, category_slug = None):
    data = BookModel.objects.all()
    category_name = CategoryModel.objects.all()
    
    if category_slug is not None:
        category = CategoryModel.objects.get(slug = category_slug)
        data = BookModel.objects.filter(category = category)
        
    return render(req,'home.html' ,{'data':data, 'category_name': category_name})

