from django.shortcuts import render,redirect
from . forms import createmusicianForm, signupForm
from .models import createmusicianModel
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

@login_required
def createmusician(req):
    if req.method == 'POST':
        form = createmusicianForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req,'Musician created Successfully!')
            return redirect('profile')
    else:
        form = createmusicianForm()
    return render (req,'musician/createmusician.html',{'form':form})

@login_required
def profile(req):
    return render (req,'musician/profile.html')

def signup(req):
    if req.method == 'POST':
        form = signupForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req,'Signed in successfully!')
            return redirect('profile')
    else:
        form = signupForm()
    return render (req,'musician/signup.html',{'form':form, 'type': 'Signup'})
            
def Userlogin(req):
    if req.method == 'POST':
        form = AuthenticationForm(req,req.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            user = authenticate(username= name, password = userpass)
            if user is not None:
                login(req,user)
                messages.success(req,'Logged in Successfully!')
                return redirect("profile")
    else:
        form = AuthenticationForm()
    return render (req,'musician/signup.html',{'form':form, 'type':'Login'})

@login_required
def Userlogout(req):
    logout(req)
    return redirect('login')

@login_required
def edit (req,id):
    musician = createmusicianModel.objects.get(pk=id)
    if req.method == 'POST':
        form = createmusicianForm(req.POST,instance=musician)
        if form.is_valid():
            form.save()
            messages.success(req,'Data edited Successfully')
            return redirect("table")
    else:
        form = createmusicianForm(instance=musician)
    return render(req,'musician/edit.html',{'form':form})