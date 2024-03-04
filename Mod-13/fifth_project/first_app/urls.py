from django.urls import path
from . import views

urlpatterns = [
    
    path('about/', views.about, name ='about'),
    path('form/', views.form, name ='form'),
    # path('django_form/', views.django_form , name ='django_form'),
    # path('django_form/', views.file_form , name ='django_form'),
    # path('django_form/', views.upload_form , name ='django_form'),
    # path('django_form/', views.student_form , name ='django_form'),
    # path('django_form/', views.teacher_form , name ='django_form'),
    # path('django_form/', views.alumni_form , name ='django_form'),
    path('django_form/', views.password_validator , name ='django_form'),
    
]
