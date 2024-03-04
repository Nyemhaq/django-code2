from django.urls import path
from . import views

urlpatterns = [
    path ('', views.home , name = 'Home'),
    path ('delete/<int:roll>', views.delete , name = 'delete'),
]
