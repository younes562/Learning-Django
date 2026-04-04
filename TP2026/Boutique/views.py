from django.shortcuts import render
from .models import Client, Produit, Commande, Detail

def liste_clients(request):
    # Récupère tous les clients de la base de données
    data_clients = Client.objects.all()
    return render(request, 'Boutique/clients.html', {'clients': data_clients})

def liste_produits(request):
    data_produits = Produit.objects.all()
    return render(request, 'Boutique/produits.html', {'produits': data_produits})

def liste_commandes(request):
    data_commandes = Commande.objects.all()
    return render(request, 'Boutique/commandes.html', {'commandes': data_commandes})

def liste_details(request):
    data_details = Detail.objects.all()
    return render(request, 'Boutique/details.html', {'details': data_details})