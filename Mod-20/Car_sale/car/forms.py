from django import forms 
from . models import Car,Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class carForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        
class signupForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs= {'id' : 'required', 'help_text' : 'False','placeholder':'Enter Your First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs= {'id' : 'required', 'help_text' : 'False','placeholder':'Enter Your Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs= {'id' : 'required','placeholder':'Enter Your Email'}),label='Email')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'help_text':False,'placeholder':'Enter Password'}),label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'help_text':False,'placeholder':'Re Enter Password'}),label='Confirm Password')
    username = forms.CharField(widget=forms.TextInput(attrs={'help_text':False,'placeholder':'Enter Your Username'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email' ]
        
class changeprofileForm(UserChangeForm):
    password = None
    username = forms.CharField(widget=forms.TextInput(attrs={'help_text':False}))
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']
        
class commentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','body']
        
      