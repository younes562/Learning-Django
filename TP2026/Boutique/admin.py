# from django.contrib import admin
# from .models import Client, Produit, Commande, Detail

# class DetailInline(admin.TabularInline):
#     model = Detail
#     extra = 1

# class CommandeAdmin(admin.ModelAdmin):
#     list_display = ('ncom', 'client', 'datecom')
#     inlines = [DetailInline]

# admin.site.register(Client)
# admin.site.register(Produit)
# admin.site.register(Detail)        # ← vérifiez que cette ligne existe
# # admin.site.register(Commande)    # ← commentée
# admin.site.register(Commande, CommandeAdmin)  # ← version PRO




from django.contrib import admin
from .models import Client, Produit, Commande, Detail

# PRO : Création d'une interface de saisie "en ligne" pour les détails
class DetailInline(admin.TabularInline):
    model = Detail
    extra = 1  # Nombre de lignes vides affichées par défaut

class CommandeAdmin(admin.ModelAdmin):
    list_display = ('ncom', 'client', 'datecom')
    # PRO : On intègre la saisie des détails directement dans la commande
    inlines = [DetailInline]
    admin.site.register(Client)
    admin.site.register(Produit)
    admin.site.register(Detail)

# مهم: غير هادي تبقى
admin.site.register(Commande, CommandeAdmin)