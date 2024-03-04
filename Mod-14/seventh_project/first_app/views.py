from django.shortcuts import render
from . forms import StudentForm

def home (req):
    if req.method == 'POST':
        form = StudentForm(req.POST) 
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = StudentForm()
    return render (req, 'first_app/home.html', {'form' : form})
