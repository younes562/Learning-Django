from django.shortcuts import render
from datetime import date

def liste_clients(request):
    clients = [
        {'ncli': 'B062', 'nom': 'goffin', 'localite': 'namur', 'compte': -3200},
        {'ncli': 'B112', 'nom': 'HANSENNE', 'localite': 'poitiers', 'compte': 1250},
        {'ncli': 'S127', 'nom': 'vanderka', 'localite': 'namur', 'compte': -4580},
    ]
    return render(request, 'Boutique/clients.html', {'clients': clients})

def liste_produits(request):
    produits = [
        {'npro': 'CS262', 'libelle': 'chev. sapin 200x6x2', 'qstock': 45},
        {'npro': 'PA45', 'libelle': 'pointe acier 45 (2k)', 'qstock': 105},
        {'npro': 'PS222', 'libelle': 'pl. sapin 200x20x2', 'qstock': 1220},
    ]
    return render(request, 'Boutique/produits.html', {'produits': produits})

def liste_commandes(request):
    commandes = [
        {'ncom': 30178, 'ncli': 'K111', 'datecom': date(2008, 12, 21)},
        {'ncom': 30179, 'ncli': 'C400', 'datecom': date(2008, 12, 23)},
    ]
    return render(request, 'Boutique/commandes.html', {'commandes': commandes})