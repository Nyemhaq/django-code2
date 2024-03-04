from django.shortcuts import render,redirect
from . forms import postForm
from .models import Post

def post (req):
    if req.method == 'POST':
        form = postForm(req.POST,req.FILES)
        if form.is_valid():
            form.save()
            return redirect ('Post')
            print(form.cleaned_data)
    else:
        form = postForm()
    return render (req, 'post/post.html',{'form':form})

def edit (req, id):
    post = Post.objects.get(pk = id)
    print  (post.title)
    form = postForm(instance=post)
    if req.method == 'POST':
        form = postForm(req.POST,req.FILES,instance=post)
        if form.is_valid():
            form.save()
            return redirect ('Home')
            print(form.cleaned_data)
    return render (req, 'post/post.html',{'form':form})

def delete(req,id):
    post = Post.objects.get(pk = id)
    post.delete()
    return redirect("Home")