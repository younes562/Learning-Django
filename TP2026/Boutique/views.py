from django.shortcuts import render, redirect, get_object_or_404
from datetime import date
from .models import Client, Produit, Commande, Detail
from .forms import ClientForm, ProduitForm, CommandeForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm


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
    data_commandes = Commande.objects.select_related('client').all()
    return render(request, 'Boutique/commandes.html', {'commandes': data_commandes})


def liste_details(request):
    data_details = Detail.objects.select_related('commande', 'produit').all()
    return render(request, 'Boutique/details.html', {'details': data_details})


def client_commandes(request, id_client):
    client = get_object_or_404(Client, ncli=id_client)
    commandes = Commande.objects.filter(client=client).prefetch_related('lignes__produit')

    return render(request, 'Boutique/client_commandes.html', {
        'client': client,
        'commandes': commandes
    })


# ================= CLIENT =================

def ajouter_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            Client.objects.create(**form.cleaned_data)
            return redirect('clients')
    else:
        form = ClientForm()

    return render(request, 'Boutique/forms.html', {
        'form': form,
        'titre': "Ajouter un Client"
    })


def modifier_client(request, pk):
    client = get_object_or_404(Client, ncli=pk)

    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            Client.objects.filter(ncli=pk).update(**form.cleaned_data)
            return redirect('clients')
    else:
        form = ClientForm(initial={
            'ncli': client.ncli,
            'nom': client.nom,
            'adresse': client.adresse,
            'localite': client.localite,
            'cat': client.cat,
            'compte': client.compte
        })

    return render(request, 'Boutique/forms.html', {
        'form': form,
        'titre': "Modifier Client"
    })


def supprimer_client(request, pk):
    client = get_object_or_404(Client, ncli=pk)

    if request.method == "POST":
        client.delete()
        return redirect('clients')

    return render(request, 'Boutique/delete_confirm.html', {
        'objet': client,
        'type': "le client"
    })


# ================= PRODUIT =================

def ajouter_produit(request):
    if request.method == "POST":
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produits')
    else:
        form = ProduitForm()

    return render(request, 'Boutique/forms.html', {
        'form': form,
        'titre': "Ajouter un Produit"
    })


def modifier_produit(request, pk):
    produit = get_object_or_404(Produit, npro=pk)

    if request.method == "POST":
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('produits')
    else:
        form = ProduitForm(instance=produit)

    return render(request, 'Boutique/forms.html', {
        'form': form,
        'titre': "Modifier Produit"
    })


def supprimer_produit(request, pk):
    produit = get_object_or_404(Produit, npro=pk)

    if request.method == "POST":
        produit.delete()
        return redirect('produits')

    return render(request, 'Boutique/delete_confirm.html', {
        'objet': produit,
        'type': "le produit"
    })


# ================= COMMANDE =================

def modifier_commande(request, pk):
    commande = get_object_or_404(Commande, ncom=int(pk))

    if request.method == "POST":
        form = CommandeForm(request.POST, instance=commande)
        if form.is_valid():
            form.save()
            return redirect('commandes')
    else:
        form = CommandeForm(instance=commande)

    return render(request, 'Boutique/forms.html', {
        'form': form,
        'titre': f"Modifier la Commande n°{pk}"
    })


def supprimer_commande(request, pk):
    commande = get_object_or_404(Commande, ncom=int(pk))

    if request.method == "POST":
        commande.delete()
        return redirect('commandes')

    return render(request, 'Boutique/delete_confirm.html', {
        'objet': commande,
        'type': "la commande"
    })
def modifier_detail(request, ncom, npro):
    detail = get_object_or_404(Detail, commande_id=ncom, produit_id=npro)

    if request.method == "POST":
        form = DetailForm(request.POST, instance=detail)
        if form.is_valid():
            form.save()
            return redirect('details')
    else:
        form = DetailForm(instance=detail)

    return render(request, 'Boutique/forms.html', {
        'form': form,
        'titre': f"Modifier Ligne (Com: {ncom}, Prod: {npro})"
    })


def supprimer_detail(request, ncom, npro):
    detail = get_object_or_404(Detail, commande_id=ncom, produit_id=npro)

    if request.method == "POST":
        detail.delete()
        return redirect('details')

    return render(request, 'Boutique/delete_confirm.html', {
        'objet': detail,
        'type': "cette ligne de commande"
    })
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()           # Crée l'utilisateur dans la base
            login(request, user)         # Connecte-le immédiatement après inscription
            return redirect('clients')
    else:
        form = RegisterForm()
    return render(request, 'Boutique/auth/register.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)         # Ouvre la session Django
            return redirect('clients')
    else:
        form = AuthenticationForm()
    return render(request, 'Boutique/auth/login.html', {'form': form})

def deconnexion(request):
    logout(request)                      # Ferme la session
    return redirect('connexion')