from django.shortcuts import render 
from post.models import Post
from category.models import Category

def home(req, category_slug = None):
    data = Post.objects.all()
    if category_slug is not None:
        category = Category.objects.get(slug = category_slug)
        data = Post.objects.filter(category = category)
    category = Category.objects.all()
    print(data)
    return render (req,'home.html',{'data':data,'category':category})