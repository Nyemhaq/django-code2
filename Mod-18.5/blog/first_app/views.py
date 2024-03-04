from django.shortcuts import render,redirect
from .forms import signupForm,userchangeForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import  authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required


@login_required
def profile(req):
    return render (req,'first_app/profile.html')

def signup(req):
    if req.method == 'POST':
        form = signupForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req,'Account Created Successfully!')
    else:
        form = signupForm(req.POST)
    return render (req,'first_app/signup.html',{'form':form, 'type':'Signup'})

def user_login(req):
    if req.method == 'POST':
        form = AuthenticationForm(req, req.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=name, password=user_pass)
            if user is not None:
                login(req,user)
                messages.success(req,'Logged in successfully!')
                return redirect('profile')
            else:
                messages.warning(req,'login information is incorrect')
                return redirect ('login')
    else:
        form = AuthenticationForm()
    return render (req,'first_app/signup.html',{'form':form, 'type':'Login'})

@login_required
def user_logout(req):
    logout(req)
    messages.warning(req,'Logout from account')
    return redirect("login")

@login_required
def edit_profile(req):
    if req.method == 'POST':
        form = userchangeForm(req.POST,instance=req.user)
        if form.is_valid:
            form.save()
            messages.success(req,'Account Updated Successfully!')
            return redirect("profile")
    else:
        form = userchangeForm(instance=req.user)
    return render (req,'first_app/edit_profile.html',{'form':form})

@login_required
def change_pass1(req):
    if req.method == "POST":
        form = PasswordChangeForm(req.user, data=req.POST)
        if form.is_valid():
            form.save()
            messages.success(req,'Password changed Successfully with Old Password!')
            update_session_auth_hash(req,form.user)
            return redirect("profile")
    else:
        form = PasswordChangeForm(user=req.user)
    return render (req,'first_app/change_pass.html',{'form':form})


@login_required
def change_pass2(req):
    if req.method == "POST":
        form = SetPasswordForm(user=req.user, data=req.POST)
        if form.is_valid():
            form.save()
            messages.success(req,'Password Changed Successfully without Old password!')
            update_session_auth_hash(req,form.user)
            return redirect ("profile")
    else:
        form = SetPasswordForm(user=req.user)
    return render (req,'first_app/change_pass.html',{'form':form})