from django.urls import path
from . import views

urlpatterns = [
    path('profile/createalbum/', views.createalbum, name = 'createalbum'),
    path('profile/table/', views.table, name = 'table'),
    path('profile/table/edit/<int:id>/', views.edit_table, name = 'edit'),
    path('profile/table/delete/<int:id>/', views.delete_table, name = 'delete'),
]
