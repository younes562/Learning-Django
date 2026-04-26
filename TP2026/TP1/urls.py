from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('admin/', admin.site.urls),
    path('boutique/', include('Boutique.urls')),  # ← Boutique pas TP1
    
]