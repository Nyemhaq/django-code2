from django.contrib import admin
from django.urls import path,include
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("book.urls")),
    path('', include("accounts.urls")),
    path('', include("borrow_transactions.urls")),
    path('', views.home, name='home'),
    path('category/<slug:category_slug>/', views.home,name="category_wise_car"),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)