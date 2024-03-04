from django import forms
from . models import createmusicianModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class createmusicianForm(forms.ModelForm):   
    class Meta:
        model = createmusicianModel
        fields = '__all__'
        
class signupForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'})) 
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'})) 
    username = forms.CharField(widget=forms.TextInput(attrs={'id':'required','help_text':False})) 
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'help_text':False}),label="Password") 
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'help_text':False}),label="Confirm Password") 
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']
        