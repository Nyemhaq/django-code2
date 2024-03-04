from django.shortcuts import render 
from post.models import Post

def home(req):
    data = Post.objects.all()
    print(data)
    return render (req,'home.html',{'data':data})