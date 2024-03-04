from django import forms 
from . models import StudentModel 

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        labels = {
            'roll' : 'Student Roll',
            'name' : 'Student Name',
            'email' : 'Student Email'
        }
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder':'Enter your name'}),
            'email' : forms.EmailInput(attrs={'placeholder':'Enter your email'})
        }
        help_texts = {
            'roll' : 'Roll must start with 110',
            'address' : 'Write your detailed address'
        }
        error_messages = {
            'name' : {'required' : 'Your name is required'}
        }