from django.shortcuts import render
from car.models import Car   
from brand.models import Brand

def home(req, brand_slug = None):
    data = Car.objects.all()
    brand_name = Brand.objects.all()
    
    if brand_slug is not None:
        brand = Brand.objects.get(slug = brand_slug)
        data = Car.objects.filter(Brand = brand)
    
    return render(req,'home.html',{'data':data, 'brand_name': brand_name})

def about(req):
    return render(req,'about.html')

def contact_us(req):
    return render(req,'contact_us.html')  