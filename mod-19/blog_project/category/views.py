from django.shortcuts import render,redirect
from . forms import categoryForm
def category (req):
    if req.method == 'POST':
        form = categoryForm(req.POST,req.FILES)
        if form.is_valid():
            form.save()
            return redirect ('Category')
            print(form.cleaned_data)
    else:
        form = categoryForm()
    return render (req, 'category/category.html',{'form':form})
