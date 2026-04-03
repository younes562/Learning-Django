from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.liste_clients, name='clients'),
    path('produits/', views.liste_produits, name='produits'),
    path('commandes/', views.liste_commandes, name='commandes'),
]