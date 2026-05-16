from django.contrib import admin
from .models import Client,Produit,Commande,Detail


admin.site.register(Client)
admin.site.register(Produit)
admin.site.register(Commande)
admin.site.register(Detail)


#pro:creatin d'un interface de saise "en ligne" pour les details
class DetailInline(admin.TabularInline):
    model=Detail
    extra=1

class commandeAdmin(admin.ModelAdmin):
    list_display=('ncom','client','datecom')
    inlines=[DetailInline]








