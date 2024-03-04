from django.urls import path
from .import views 

urlpatterns = [
    path('profile/',views.profile,name='profile' ),
    path('signup/',views.signup,name='signup' ),
    path('login/',views.user_login,name='login' ),
    path('profile/logout/',views.user_logout,name='logout' ),
    path('profile/edit_profile/',views.edit_profile,name='edit_profile' ),
    path('profile/change_password_with_old_pass/',views.change_pass1,name='change_pass1' ),
    path('profile/change_password_without_old_pass/',views.change_pass2,name='change_pass2' ),
    
]
