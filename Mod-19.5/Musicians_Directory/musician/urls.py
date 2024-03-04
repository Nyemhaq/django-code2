from django.urls import path
from . import views

urlpatterns = [
    path('profile/createmusician/', views.createmusician, name = 'createmusician'),
    path('signup/', views.signup, name = 'signup'),
    path('login/', views.Userlogin, name = 'login'),
    path('profile/logout/', views.Userlogout, name = 'logout'),
    path('profile/', views.profile, name = 'profile'),
    path('profile/edit/<int:id>/', views.edit, name = 'edit2'),
]
