from django import forms
from django.core import validators

class contactForm (forms.Form):
    name = forms.CharField(label="Username")
    email = forms.EmailField(initial="nyem12@gmail.com")
    age = forms.IntegerField(required=False)
    weight = forms.FloatField(disabled=True)
    balance = forms.DecimalField()
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    appoinment = forms.DateTimeField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
    check = forms.BooleanField()
    CHOICES = [('S',"Small"),('M',"Medium"),('L',"Large")]
    size = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect())
    MEAL = [('P','Pizza'),('B','Burger'),('C','CocaCola')]
    food = forms.MultipleChoiceField(choices=MEAL,help_text="you must choose at least one food",widget=forms.CheckboxSelectMultiple())
    details = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'write your thoughts'}))
    
class fileForm (forms.Form):
    name = forms.CharField()
    file = forms.FileField()
    
class uploadForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    file = forms.FileField()
    
class studentForm(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    def clean_name (self):
        valname = self.cleaned_data['name']
        if len(valname) < 10:
            raise forms.ValidationError("Name must contain at least 10 character")
        return valname
    def clean_email (self):
        valemail = self.cleaned_data['email']
        if '.com' not in valemail:
            raise forms.ValidationError("Email must contain .com")
        return valemail
  
class teacherForm(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    def clean (self):
        cleaned_data = super().clean()
        valname = self.cleaned_data['name']
        valemail = self.cleaned_data['email']
        if len(valname) < 10:
            raise forms.ValidationError("Name must contain at least 10 character")
        if ".com" not in valemail:
            raise forms.ValidationError("Email must contain .com")
        
        
def length_check(value):
    if len(value) < 10:
        raise forms.ValidationError("Must be above 10 characters")
          
class alumniForm(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(10,message="Name must contain not more than 10 character")])
    email = forms.EmailField(validators=[validators.EmailValidator(message="Enter a valid email")])
    age = forms.IntegerField(validators=[validators.MinValueValidator(10,message="age must above 10"),validators.MaxValueValidator(35,message="Age must less than 35")])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['jpg'],message='file must be jpg')])
    text = forms.CharField(validators=[length_check])
    
    
class passwordvalidatorForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        valpass = self.cleaned_data['password']
        valconpass = self.cleaned_data['confirm_password']
        if valpass != valconpass:
            raise forms.ValidationError("password doesn't match")