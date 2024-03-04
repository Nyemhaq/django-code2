from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class signupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'id':'required', 'help_text':False,'placeholder':'Enter your username','initial':None}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required','help_text':False,'placeholder':'Enter your first name','initial':None})) 
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required','help_text':False,'placeholder':'Enter your last name','initial':None}))   
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id':'required','help_text':False,'placeholder':'Enter your email','initial':None}))   
    password1 = forms.CharField(widget=forms.TextInput(attrs={'id':'required','help_text':False,'placeholder':'Enter password'}), label='Password')   
    password2 = forms.CharField(widget=forms.TextInput(attrs={'id':'required','help_text':False,'placeholder':'Re enter password'}),label='Confirm Password')   
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        
class userchangeForm(UserChangeForm):
    password = None
    username = forms.CharField(widget=forms.TextInput(attrs={'help_text':False}))
    class Meta:
         model = User
         fields = ['username','first_name','last_name','email']