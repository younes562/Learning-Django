from django.contrib import admin
from .models import Client, Produit, Commande , Detail

admin.site.register(Client)
admin.site.register(Commande)
admin.site.register(Produit)
admin.site.register(Detail)