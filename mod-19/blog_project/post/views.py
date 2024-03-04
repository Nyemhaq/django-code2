from django.shortcuts import render,redirect
from . forms import postForm,commentForm
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from . import models,forms
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

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

""" 
 -- -- -- class based view -- -- --
"""

@method_decorator(login_required, name='dispatch')
class addpostCreateView(CreateView):
    model = models.Post
    form_class = forms.postForm
    template_name = 'post/post.html'
    success_url = reverse_lazy('profile')
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class editpostview(UpdateView):
    model = models.Post
    form_class = forms.postForm
    template_name = 'post/post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("profile")

@method_decorator(login_required, name='dispatch')   
class deletepostview(DeleteView):
    model = models.Post
    template_name = 'post/delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')
    
class postdetailView(DetailView):
    model = models.Post
    template_name = 'post/detail_post.html'
    pk_url_kwarg = 'id'
    
    def post(self, request, *args, **kwargs):
        form = forms.commentForm(data=self.request.POST)
        post = self.get_object()
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comment = post.comment.all()
        form = forms.commentForm()
            
        context['comment']= comment
        context['form']=form
        return context
            
            