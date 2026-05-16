from django.urls import path
from . import views

urlpatterns=[
    path('clients/',views.list_clients,name='clients'),
    path('products/',views.list_produits,name='products'),
    path('commandes/',views.list_commandes,name='commandes'),
    path('details/',views.liste_details,name='details'),
    path('client/<str:id_client>/',views.client_commandes,name="client_commandes"),

    #Clients
    path('client/ajouter',views.ajouter_client,name="ajouter_client"),
    path('client/modifier/<str:pk>/',views.modifier_client,name="modifier_client"),
    path('client/supprimer/<str:pk>/',views.supprimer_client,name='supprimer_client'),

    #produits
    path('produit/ajouter/',views.ajouter_produit,name='ajouter_produit'),
    path('produit/modifier/<str:pk>/',views.modifier_produit,name='modifier_produit'),
    path('produit/supprimer/<str:pk>/',views.supprimer_produit,name='supprimer_produit'),

    #commandes
    path('commande/ajouter/',views.ajouter_commande,name='ajouter_commande'),
    path('commande/modifier/<str:pk>',views.modifier_commande,name='modifier_commande'),
    path('commande/supprimer/<str:pk>',views.supprimer_commande,name='supprimer_commande'),

    #details
    path('detail/ajouter/',views.ajouter_detail,name='ajouter_detail'),
    path('detail/modifier/<int:ncom>/<str:npro>/', views.modifier_detail, name='modifier_detail'),
    path('detail/supprimer/<int:ncom>/<str:npro>/',views.supprimer_detail,name='supprimer_detail'), 

    #version PRO
    path('update/<int:ob>/<str:pk>/<str:pk2>/',views.update,name="update"),
    path('delete/<int:ob>/<str:pk>/<str:pk2>/',views.delete,name="delete"),

    #url d'authentification
    path('register/',views.register,name='register'),
    path('login/',views.connexion,name='connexion'),
    path('logout/',views.deconnexion,name='deconnexion'),

    path('tableau_bord/',views.tableau_bord_admin,name='tableau_bord'),
    path('profile/',views.profile,name='profile')
]