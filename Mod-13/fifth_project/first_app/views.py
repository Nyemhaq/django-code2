from django.shortcuts import render
from . forms import contactForm, fileForm, uploadForm, studentForm, teacherForm,alumniForm,passwordvalidatorForm

def about (req):
      if req.method == 'POST':
        print (req.POST)
        name = req.POST.get('username')
        email = req.POST.get('useremail')
        ratings = req.POST.get('ratings')
        return render (req, 'first_app/about.html',{'name':name,'email':email,'ratings':ratings})
      else:
        return render (req, 'first_app/about.html')
def form (req):
    return render (req, 'first_app/form.html')
    
def django_form (req):
    form = contactForm(req.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render (req, 'first_app/django_form.html',{'form':form})
  
def file_form (req):
  if req.method == 'POST':
    form = fileForm (req.POST, req.FILES)
    if form.is_valid():
      file = form.cleaned_data['file']
      with open ('first_app/upload/' + file.name, 'wb+') as destination:
        for chunk in file.chunks():
          destination.write(chunk)
      print(form.cleaned_data)
      return render (req, 'first_app/django_form.html',{'form':form})
  else:
    form = fileForm()
  return render (req, 'first_app/django_form.html',{'form':form})


def upload_form (req):
  if req.method == 'POST':
    form = uploadForm(req.POST, req.FILES)
    if form.is_valid():
      file = form.cleaned_data['file']
      with open ('first_app/upload/' + file.name, 'wb+') as destination:
        for chunk in file.chunks():
          destination.write(chunk)
      print(form.cleaned_data)
      return render (req,'first_app/django_form.html', {'form':form})
  else:
    form = uploadForm ()
  return render (req,'first_app/django_form.html', {'form':form})


def student_form (req):
  if req.method == 'POST':
    form = studentForm(req.POST)
    if form.is_valid():
      print(form.cleaned_data)
      return render (req,'first_app/django_form.html',{'form':form})
  else:
    form = studentForm()
  return render (req,'first_app/django_form.html',{'form':form})


def teacher_form (req):
  if req.method == 'POST':
    form = teacherForm(req.POST)
    if form.is_valid():
      print(form.cleaned_data)
      return render (req,'first_app/django_form.html',{'form':form})
  else:
    form = teacherForm()
  return render (req,'first_app/django_form.html',{'form':form})


def alumni_form (req):
  if req.method == 'POST':
    form = alumniForm(req.POST, req.FILES)
    if form.is_valid():
      file = form.cleaned_data['file']
      with open ('first_app/upload/' + file.name, 'wb+') as destination:
        for chunk in file.chunks():
          destination.write(chunk)
      print(form.cleaned_data)
      return render (req,'first_app/django_form.html',{'form':form})
  else:
    form = alumniForm()
  return render (req,'first_app/django_form.html',{'form':form})

def password_validator(req):
  if req.method == 'POST':
    form = passwordvalidatorForm(req.POST, req.FILES)
    if form.is_valid():
      print(form.cleaned_data)
      return render (req,'first_app/django_form.html',{'form':form})
  else:
    form = passwordvalidatorForm()
  return render (req,'first_app/django_form.html',{'form':form})