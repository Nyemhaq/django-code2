from django.urls import path
from . import views

urlpatterns = [
    # path('', views.post, name='Post'),
    path('addpost/', views.addpostCreateView.as_view(), name='Post'),
    # path('edit/<int:id>/', views.edit, name='edit'),
    path('edit/<int:id>/', views.editpostview.as_view(), name='edit'),
    # path('delete/<int:id>/', views.delete, name='delete'),    
    path('delete/<int:id>/', views.deletepostview.as_view(), name='delete'),    
    path('post/details_post/<int:id>/', views.postdetailView.as_view(), name='detail_post'),    
]
