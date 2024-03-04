from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class signupForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs= {'id' : 'required', 'help_text' : 'False'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs= {'id' : 'required', 'help_text' : 'False'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'help_text':False}),label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'help_text':False}),label='Confirm Password')
    username = forms.CharField(widget=forms.TextInput(attrs={'help_text':False}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        
class chagerprofileForm(UserChangeForm):
    password = None
    username = forms.CharField(widget=forms.TextInput(attrs={'help_text':False}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
    