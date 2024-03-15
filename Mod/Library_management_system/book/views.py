from django.shortcuts import render,redirect
from .forms import signupForm,changeprofileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from .models import BookModel
def signup(req):
    if req.method == "POST":
        form = signupForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req,"sigup successfully")
            return redirect("login")
    else:
        form = signupForm()
    return render (req,'book/signup.html',{'form':form, 'type': 'Signup'})

def user_login(req):
    if req.method == 'POST':
        form = AuthenticationForm(req,req.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username = name , password = user_pass)
            if user is not None:
                login(req,user)
                messages.success(req,"logged in successfully")
                return redirect("profile")
    else:
        form = AuthenticationForm()
    return render (req,'book/signup.html',{'form':form, 'type':'Login'})

@login_required
def profile(req):
    return render (req,'book/profile.html')

@login_required
def user_logout(req):
    logout(req)
    return redirect("login")

@login_required
def edit_profile(req):
    if req.method == 'POST':
        form = changeprofileForm(req.POST, instance = req.user)
        if form.is_valid():
            form.save()
            messages.success(req,'Profile Updated Successfully!')
            return redirect('profile')
    else:
        form = changeprofileForm(instance = req.user)
    return render (req,'book/edit_profile.html',{'form':form})
        
@login_required
def change_password(req):
    if req.method == "POST":
        form = PasswordChangeForm(req.user, data=req.POST)
        if form.is_valid():
            form.save()
            messages.success(req,'Password Updated Successfully!')
            update_session_auth_hash(req,form.user)
            return redirect("profile")
    else:
        form = PasswordChangeForm(user=req.user)
    return render (req,'book/change_pass.html',{'form':form})

class detailView(DetailView):
    model = BookModel
    template_name = 'book/details.html'
    pk_url_kwarg = 'id'
    
    # def post(self, request, *args, **kwargs):
    #     form = commentForm(data=self.request.POST)
    #     post = self.get_object()
    #     if form.is_valid():
    #         new_comment = form.save(commit=False)
    #         new_comment.post = post
    #         new_comment.save()
    #     return self.get(request, *args, **kwargs)

    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     post = self.object
    #     comment = post.comment.all()
    #     form = forms.commentForm()
            
    #     context['comment']= comment
    #     context['form']=form
    #     return context
    
@login_required
def buy_now(req,id):
    if req.method == 'POST':
        book = BookModel.objects.get(pk=id)
        if book.total_car > 0:
            book.total_car -= 1
            book.save()
            
            data = BookModel.objects.filter(pk=id)
            messages.success(req,'Book bought Successfully!')
            return render(req,"book/profile.html",{'data':data})
            
        else:
            messages.warning(req,'Sorry! Book is not Available :(')
        return redirect("profile")
    else:
        return render(req,'book/details.html')