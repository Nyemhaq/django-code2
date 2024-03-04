from django.shortcuts import render, redirect
from . import models

def home(req):
    student = models.Student.objects.all()
    print(student)
    return render (req,'first_app/home.html',{'data': student})

def delete(req,roll):
    std = models.Student.objects.get(pk = roll).delete()
    return redirect("Home")