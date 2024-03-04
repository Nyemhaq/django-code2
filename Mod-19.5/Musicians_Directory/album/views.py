from django.shortcuts import render,redirect
from . forms import albumForm
from django.contrib import messages
from .models import albumModel
from django.contrib.auth.decorators import login_required

@login_required
def createalbum(req):
    if req.method == 'POST':
        form = albumForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req,'Album Created Successfully!')
            return redirect ('table')
    else:
        form = albumForm()
    return render(req,'album/create_album.html',{'form':form})

def table(req):
    data = albumModel.objects.all()
    return render(req,'album/table.html',{'data':data})

@login_required
def edit_table(req,id):
    album = albumModel.objects.get(pk = id)
    if req.method == "POST":
        form = albumForm(req.POST,instance=album)
        if form.is_valid():
            form.save()
            messages.success(req, "Data edited succcessfully!")
            return redirect("table")
    else:
        form = albumForm(instance=album)
    return render (req,'album/edit.html',{'form':form})

@login_required
def delete_table(req,id):
    album = albumModel.objects.get(pk = id)
    album.delete()
    return redirect("table")