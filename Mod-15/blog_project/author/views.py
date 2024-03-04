from django.shortcuts import render,redirect
from . forms import authorForm

def author (req):
    if req.method == 'POST':
        form = authorForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect ('Author')
            print(form.cleaned_data)
    else:
        form = authorForm()
    return render (req, 'author/author.html', {'form':form})
