from django.shortcuts import render,redirect
from .forms import registerForm,changeForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash

def home(req):
    return render(req,'first_app/home.html')


def signup (req):
    if not req.user.is_authenticated:
        if req.method == 'POST':
            form = registerForm(req.POST)
            if form.is_valid():
                messages.success(req,'Account Created Successfully!')
                form.save()
                print (form.cleaned_data)
        else:
            form = registerForm()
        return render (req,'first_app/signup.html',{'form':form})
    else:
        return redirect('profile')

def userlogin(req):
    if not req.user.is_authenticated:
        if req.method == "POST":
            form = AuthenticationForm(data = req.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username = name , password = userpass)
                if user is not None:
                    login(req,user)
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render (req,'first_app/login.html',{'form':form})
    else:
        return redirect('profile')
        
def profile(req):
    if req.user.is_authenticated:
        if req.method == 'POST':
            form = changeForm(req.POST, instance = req.user)
            if form.is_valid():
                messages.success(req,'Account Updated Successfully!')
                form.save()
                print (form.cleaned_data)
        else:
            form = changeForm(instance = req.user)
        return render (req,'first_app/profile.html',{'form':form})
    else:
        return redirect('profile')

def userlogout(req):
    logout(req)
    return redirect("login")

def changepass(req):
    if req.user.is_authenticated:
        if req.method == 'POST':
            form = PasswordChangeForm(user=req.user, data=req.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash (req,form.user)
                return redirect ('profile')
        else:
            form = PasswordChangeForm(user=req.user)
        return render (req,'first_app/change_pass.html',{'form':form})
    else:
        return redirect("login")
    
def changepass2(req):
    if req.user.is_authenticated:
        if req.method == 'POST':
            form = SetPasswordForm(user=req.user, data=req.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash (req,form.user)
                return redirect ('profile')
        else:
            form = SetPasswordForm(user=req.user)
        return render (req,'first_app/change_pass.html',{'form':form})
    else:
        return redirect("login")


