from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    # path('login/', views.user_login, name='login'),
    path('login/', views.userloginview.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('logout/', views.userlogoutview.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/edit/change_password/', views.change_password, name='change_password'),
]
