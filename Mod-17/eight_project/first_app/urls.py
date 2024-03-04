from django.urls import path
from . import views

urlpatterns = [
    path('', views.home ,name = 'home' ),
    path('profile/', views.profile ,name = 'profile' ),
    path('login/', views.userlogin ,name = 'login' ),
    path('logout/', views.userlogout ,name = 'logout' ),
    path('signup/', views.signup ,name = 'signup' ),
    path('changepass/', views.changepass ,name = 'changepass' ),
    path('changepass2/', views.changepass2 ,name = 'changepass2' ),
    
]
