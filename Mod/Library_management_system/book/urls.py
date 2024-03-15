from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit_profile/', views.edit_profile, name='edit_profile'),
    path('profile/change_pass/', views.change_password, name='change_pass'),
    path('details/<int:id>/', views.detailView.as_view(), name='details'), 
    path('details/buy_now/<int:id>/', views.buy_now, name='buy_now'),     
]
