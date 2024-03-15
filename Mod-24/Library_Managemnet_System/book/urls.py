from django.urls import path
from . import views

urlpatterns = [
    # path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    # path('profile/', views.profile, name='profile'),
    path('profile/change_pass/', views.change_password, name='change_pass'),
    path('details/<int:id>/', views.details, name='details'), 
    path('profile/borrowed_book/<int:id>/', views.buy_now, name='buy_now'),
    path('profile/borrowed_book/', views.borrow_books, name='borrow_books'),
    path('review/<int:id>/', views.review, name='review'),
    path('/<int:id>', views.return_book, name='return_book'),
]
