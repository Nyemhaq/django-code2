from django.shortcuts import render,redirect
from . forms import postForm
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def post (req):
    if req.method == 'POST':
        form = postForm(req.POST,req.FILES)
        if form.is_valid():
            form.instance.author = req.user
            form.save()
            return redirect ('Home')
            print(form.cleaned_data)
    else:
        form = postForm()
    return render (req, 'post/post.html',{'form':form})


@login_required
def edit (req, id):
    post = Post.objects.get(pk = id)
    form = postForm(instance=post)
    if req.method == 'POST':
        form = postForm(req.POST,instance=post)
        if form.is_valid():
            form.instance.author = req.user
            messages.success(req,'Post Edited Successfully!')
            form.save()
            return redirect ('profile')
    return render (req, 'post/post.html',{'form':form})

@login_required
def delete(req,id):
    post = Post.objects.get(pk = id)
    post.delete()
    return redirect("Home")