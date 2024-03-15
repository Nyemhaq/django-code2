from django.shortcuts import render,redirect
from .forms import signupForm
from django.contrib import messages 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

def signup(req):
    if req.method == "POST":
        form = signupForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req,'Register account Successfully!')
            return redirect("login")
    else:
        form= signupForm()
    return render(req,'book/register.html',{'form' : form, 'type' : 'Signup'})


def user_login(req):
    if req.method == 'POST':
        form = AuthenticationForm(req,req.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username = name , password = user_pass)
            if user is not None:
                login(req,user)
                messages.success(req,'Logged in Successfully!')
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(req,'book/register.html',{'form':form, 'type' : 'Login'})


def profile(req):
    return render(req,'book/profile.html')
