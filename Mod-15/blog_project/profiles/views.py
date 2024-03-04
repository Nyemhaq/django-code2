from django.shortcuts import render,redirect
from .forms import profileForm
def profiles (req):
    if req.method == 'POST':
        form = profileForm(req.POST,req.FILES)
        if form.is_valid():
            form.save()
            return redirect ('Profiles')
            print(form.cleaned_data)
    else:
        form = profileForm()
    return render (req, 'profiles/profiles.html',{'form':form})
