from django.urls import path
from . import views

urlpatterns = [
    # Listes
    path('clients/', views.liste_clients, name='clients'),
    path('produits/', views.liste_produits, name='produits'),
    path('commandes/', views.liste_commandes, name='commandes'),
    path('details/', views.liste_details, name='details'),

    # IMPORTANT: ajouter قبل أي route عامة
    path('client/ajouter/', views.ajouter_client, name='ajouter_client'),
    path('client/modifier/<str:pk>/', views.modifier_client, name='modifier_client'),
    path('client/supprimer/<str:pk>/', views.supprimer_client, name='supprimer_client'),

    # خاصها تبقى فالآخر ديما
    path('client/<str:id_client>/', views.client_commandes, name='client_commandes'),

    # Produits
    path('produit/ajouter/', views.ajouter_produit, name='ajouter_produit'),
    path('produit/modifier/<str:pk>/', views.modifier_produit, name='modifier_produit'),
    path('produit/supprimer/<str:pk>/', views.supprimer_produit, name='supprimer_produit'),

    # ================= DETAIL (ADDED) =================
    path('detail/modifier/<int:ncom>/<str:npro>/', views.modifier_detail, name='modifier_detail'),
    path('detail/supprimer/<int:ncom>/<str:npro>/', views.supprimer_detail, name='supprimer_detail'),

    # URLs d'authentification
    path('register/', views.register, name='register'),
    path('login/',    views.connexion, name='connexion'),
    path('logout/',   views.deconnexion, name='deconnexion'),

    # VERSION PRO : Routes génériques (commentées)
    # path('update/<int:ob>/<str:pk>/<str:pk2>/', views.update, name="update"),
    # path('delete/<int:ob>/<str:pk>/<str:pk2>/', views.delete, name="delete"),
]