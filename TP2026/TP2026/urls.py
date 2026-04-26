
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('about/', views.about, name='about'),
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('boutique/', include('Boutique.urls')),
    path('', include('TP1.urls')),
    path('gestion/', include('Gestion.urls')),

]

"""
from django.contrib import admin
from django.urls import path, include
from TP1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('TP1.urls')),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('gestion/', include('Gestion.urls')),
    path('boutique/', include('Boutique.urls')),
]