from django.shortcuts import render,redirect
from . forms import signupForm,chagerprofileForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from post.models import Post
from post.forms import postForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

def signup (req):
    if req.method == 'POST':
        form = signupForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            messages.success(req, 'Account Created Successfully!')
            return redirect ('signup')
            print(form.cleaned_data)
    else:
        form = signupForm()
    return render (req, 'author/signup.html', {'form':form ,'type' : 'Signup'})

def user_login(req):
    if req.method == 'POST':
        form = AuthenticationForm(req, req.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username = name, password = user_pass)
            if user is not None:
                login(req, user)
                messages.success(req,'Logged in Successfully!')
                return redirect('edit_profile')
            else:
                messages.warning(req, 'login info in incorrect')
                return redirect('signup')
    else:
        form = AuthenticationForm()
    return render (req,'author/signup.html',{'form':form , 'type' : 'Login'})

@login_required
def edit_profile(req):
    if req.method == "POST":
        form = chagerprofileForm(req.POST, instance = req.user)
        if form.is_valid():
            form.save()
            messages.success(req,'Account Updated Successfully!')
            return redirect ('edit_profile')
    else:
        form = chagerprofileForm(instance = req.user)
    return render (req,'author/edit_profile.html',{'form':form})


@login_required
def change_password(req):
    if req.method == "POST":
        form = PasswordChangeForm(req.user, data=req.POST)
        if form.is_valid():
            form.save()
            messages.success(req,'Password Updated Successfully!')
            update_session_auth_hash(req,form.user)
            return redirect("edit_profile")
    else:
        form = PasswordChangeForm(user=req.user)
    return render (req,'author/change_pass.html',{'form':form})
        
        
@login_required
def profile(req):
    data = Post.objects.filter(author = req.user)
    return render (req,'author/profile.html',{'data':data})

def user_logout(req):
    logout(req)
    return redirect("login")

""" 
 -- -- -- class based view -- -- -- 
"""

class userloginview(LoginView):
    template_name = 'author/signup.html'
    
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
""" 
-- -- -- If class based logout doesn't work then use function base logout -- -- -- 
"""
    
class userlogoutview(LogoutView):
    success_url = reverse_lazy('login')
    # def get_success_url (self):
    #     return reverse_lazy("login")