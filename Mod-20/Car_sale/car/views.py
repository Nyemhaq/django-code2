from django.shortcuts import render,redirect
from .forms import carForm,signupForm,commentForm,changeprofileForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm 
from django.contrib.auth.models import User  
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from . import models,forms
from .models import Car,UserBuyCar
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy

def signup (req):
    if req.method == 'POST':
        form = signupForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req,"Account created successfully!")
            return redirect("login")
    else:
        form = signupForm()
    return render(req,'car/signup.html',{'form':form, 'type':'Signup'})

@login_required
def profile(req):
    return render(req,'car/profile.html')

def user_login(req):
    if req.method == 'POST':
        form = AuthenticationForm(req, req.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            user = authenticate(username = name, password = userpass)
            if user is not None:
                login(req,user)
                messages.success(req,'Logged in Successfully !')
                return redirect("profile")
    else:
        form = AuthenticationForm()
    return render (req,'car/signup.html',{'form':form ,'type':'Login'})

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
    return render (req,'car/edit_profile.html',{'form':form})

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
    return render (req,'car/change_pass.html',{'form':form})
        
    

@login_required
def user_logout(req):
    logout(req)
    return redirect("login")


class detailView(DetailView):
    model = models.Car
    template_name = 'car/details.html'
    pk_url_kwarg = 'id'
    
    def post(self, request, *args, **kwargs):
        form = commentForm(data=self.request.POST)
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
            
@login_required
def buy_now(req,id):
    if req.method == 'POST':
        car = Car.objects.get(pk=id)
        if car.total_car > 0:
            car.total_car -= 1
            car.save()
            
            data = models.Car.objects.filter(pk=id)
            messages.success(req,'Car bought Successfully!')
            return render(req,"car/profile.html",{'data':data})
            
        else:
            messages.warning(req,'Sorry! Car is not Available :(')
        return redirect("profile")
    else:
        return render(req,'car/details.html')
        
class userloginview(LoginView):
    template_name = 'car/signup.html'
    
    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request,'Logged in Successfully')
        return super().form_valid(form)
    
    def form_invalid (self,form):
        messages.success(self.request,'Log in information is incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['type'] = 'Login'
        return context
    
    class userlogoutview(LogoutView):
        success_url = reverse_lazy('login')