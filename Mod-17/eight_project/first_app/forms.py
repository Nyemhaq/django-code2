from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms

class registerForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'help_text':'False'}),initial="")
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}),initial="")
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}),initial="")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id' : 'required'}),initial="")
    password1 = forms.CharField(label="Password" , widget=forms.PasswordInput(attrs={'help_text':'False'}),initial="")
    password2 = forms.CharField(label="Confirm Password" , widget=forms.PasswordInput(attrs={'help_text':'False'}),initial="")
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        
class changeForm(UserChangeForm):
    password = None
    username = forms.CharField(widget=forms.TextInput(attrs={'help_text':'False'}),initial="")
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']