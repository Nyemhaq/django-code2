from django.shortcuts import render
from datetime import datetime, timedelta
def home(req):
    response = render (req,'first_app/home.html')
    response.set_cookie('name','mahedi',max_age=10) #max_age defines after how many second the cookie will be deleted
    response.set_cookie('name','mahedi', expires=datetime.utcnow()+timedelta(days=7)) #it will delete cookie after 7 days
    return response

def get_cookie(req):
    name = req.COOKIES.get('name')
    print(name)
    return render (req,'first_app/get_cookie.html',{'name':name})

def del_cookie(req):
    response = render (req,'first_app/del_cookie.html')
    response.delete_cookie('name')
    return response

def set_session(req):
    data ={
        'name':'Mahedy',
        'age' : 27,
        'language' : 'Bangla'
    }
    req.session.update(data)
    return render(req,'first_app/session.html')

def get_session(req):
    name = req.session.get('name')
    age = req.session.get('age')
    language = req.session.get('language')
    return render (req, 'first_app/get_session.html', {'name':name, 'age':age, 'language':language})


def delete_session(req):
    # del req.session['name'] for name delete only
    req.session.flush() #for all delete
    return render (req,'del_session.html')
