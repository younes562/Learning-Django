from django import forms
from .models import Client, Produit, Commande, Detail
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm 
from django.contrib.auth.models import User

# Formulaire manuel (standard) pour Client
class ClientForm(forms.Form):
    ncli = forms.CharField(label="Numéro Client", max_length=10)
    nom = forms.CharField(label="Nom Complet", max_length=100)
    adresse = forms.CharField(label="Adresse", max_length=200)
    localite = forms.CharField(label="Ville", max_length=100)
    cat = forms.CharField(label="Catégorie", max_length=2, required=False)
    compte = forms.DecimalField(label="Solde Compte", max_digits=10, decimal_places=2)

# Formulaire automatique (ModelForm) pour les autres
class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = '__all__'

class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = '__all__'

class DetailForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = '__all__'
class ClientForm1(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


# Formulaire d'inscription (hérite de UserCreationForm fourni par Django)
class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='Adresse Email', required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
# Formulaire de connexion (on réutilise directement celui de Django)
# AuthenticationForm est importé ci-dessus, pas besoin d'en créer un nouveau