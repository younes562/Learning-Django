from django.shortcuts import render,get_object_or_404,redirect
from .models import Client,Produit,Commande,Detail
from .forms import ClientForm,ClientForm1,ProduitForm,CommandeForm,DetailForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied
from django.views.decorators.http import require_POST
LOGIN_URL = '/boutique/login/'


# definition de condition d'acces
def est_adminstrateur(user):
    return user.groups.filter(name='adminstrateur').exists() or user.is_superuser

@login_required(login_url=LOGIN_URL)
def list_clients(request):
    data_clients=Client.objects.all()
    return render(request,'Boutique/clients.html',{'clients':data_clients})

@login_required(login_url=LOGIN_URL)
def list_produits(request):
    data_produits=Produit.objects.all()
    return render(request,'Boutique/prodects.html',{'produits':data_produits})

@login_required(login_url=LOGIN_URL)
def list_commandes(request):
    data_commandes=Commande.objects.select_related('client').all()
    return render(request,'Boutique/commandes.html',{'commandes':data_commandes})

@login_required(login_url=LOGIN_URL)
def liste_details(request):
    data_details=Detail.objects.select_related('commande','produit').all()
    return render(request,'Boutique/details.html',{'details':data_details})


def client_commandes(request,id_client):
    client=get_object_or_404(Client,ncli=id_client)

    commandes=Commande.objects.filter(client=client).prefetch_related('lignes__produit')

    return render(request,'Boutique/client_commandes.html',{
        'client':client,
        'commandes':commandes
    })

def ajouter_client(request):
    if request.method=="POST":
        form=ClientForm(request.POST)      
        if form.is_valid():
            #Creation manuelle car c'est un forms.Form
            Client.objects.create(**form.cleaned_data)
            return redirect('clients')
    else:
        form=ClientForm()   
    return render(request,'Boutique/forms.html',{'form':form,'titre':"ajouter un Client"})
    

def modifier_client(request,pk):
    client = get_object_or_404(Client,ncli=pk)
    if request.method=="POST":
        form=ClientForm(request.POST)
        if form.is_valid():
            #misa a jour manuelle pour un form standard
            Client.objects.filter(ncli=pk).update(**form.cleaned_data)
            return redirect('clients')
    else:
        form=ClientForm(initial={
            'ncli':client.ncli,'nom':client.nom,'adresse':client.adresse,'localite':client.localite,'cat':client.cat,'compte':client.compte
        })
    return render(request,'Boutique/forms.html',{'form':form,'titre':"modifier client"})

@permission_required('Boutique.delete_client', login_url=LOGIN_URL)
def supprimer_client(request,pk):
    client = get_object_or_404(Client,ncli=pk)
    if request.method=="POST":
        client.delete()
        return redirect('clients')
    return render(request,'Boutique/delete_confirm.html',{'objet':client,'type':"le client"})


def ajouter_produit(request):
    if request.method=="POST":
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form=ProduitForm()
    return render(request,'Boutique/forms.html',{'form':form,'titre':"Ajouter un Produit"})
        

def modifier_produit(request,pk):
    produit=get_object_or_404(Produit,npro=pk)
    if request.method=="POST":
        form=ProduitForm(request.POST,instance=produit)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form=ProduitForm(instance=produit)
    return render(request,'Boutique/forms.html',{'form':form,"titre":"modifier produit"})    

def supprimer_produit(request,pk):
    produit=get_object_or_404(Produit,npro=pk)
    if request.method=="POST":
        produit.delete()
        return redirect('products')
    return render(request,'Boutique/delete_confirm.html',{'objet':produit,"type":"le produit"})


def ajouter_commande(request):
    if request.method=="POST":
        form=CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('commandes')
    else:
        form=CommandeForm()
    return render(request,'Boutique/forms.html',{'form':form,'titre':"Ajouter une Commande"})


def modifier_commande(request,pk):
    commande=get_object_or_404(Commande,ncom=int(pk))

    if request.method == 'POST':
        form=CommandeForm(request.POST,instance=commande)
        if form.is_valid():
            form.save()
            return redirect('commandes')
    else:
        form=CommandeForm(instance=commande)
    
    return render(request,'Boutique/forms.html',{
        'form':form,
        'titre':f"modifier la commmande n{pk}"
    })


def supprimer_commande(request,pk):
    commande=get_object_or_404(Commande,ncom=pk)
    if request.method=="POST":
        commande.delete()
        return redirect('commandes')
    return render(request,'Boutique/delete_confirm.html',{'objet':commande,"type":"la commande"})


def ajouter_detail(request):
    if request.method=="POST":
        form=DetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details')
    else:
        form=DetailForm()
    return render(request,'Boutique/forms.html',{'form':form,'titre':"Ajouter un Detail"})


def modifier_detail(request,ncom,npro):
    detail=get_object_or_404(Detail,commande_id=ncom,produit_id=npro)
    if request.method=="POST":
        form=DetailForm(request.POST,instance=detail)
        if form.is_valid():
            form.save()
            return redirect('details')
    else:
        form=DetailForm(instance=detail)

    return render(request,'Boutique/forms.html',{
        'form':form,
        'titre':f"Modifier ligne (Com:{ncom},Prod:{npro})"
    })

def supprimer_detail(request,ncom,npro):
    detail=get_object_or_404(Detail,commande_id=ncom,produit_id=npro)

    if request.method=="POST":
        detail.delete()
        return redirect('details')
    
    return render(request,'Boutique/delete_confirm.html',{
        'objet':detail,
        'type':"cette lign de commande"
    })




MODEL_NAMES={
    0:'client',
    1:'commande',
    2:'detail',
    3:'produit',
}

@login_required(login_url=LOGIN_URL)
def update(request,ob,pk,pk2):
    model_name=MODEL_NAMES.get(ob)
    permission=f'Boutique.change_{model_name}'

    if not request.user.has_perm(permission):
        return render(request,'Boutique/403.html')
    
    config={
        0:(Client,ClientForm1,'ncli','clients'),
        1:(Commande,CommandeForm,'ncom','commandes'),
        3:(Produit,ProduitForm,'npro','products'),
    }

    if ob==2:
        instance=get_object_or_404(Detail,commande_id=int(pk),produit_id=pk2)
        form_class=DetailForm
        redir='details'
    else:
        model,form_class,pk_field,redir=config[ob]
        lookup_value = int(pk) if ob==1 else pk
        instance=get_object_or_404(model,**{pk_field:lookup_value})
    if request.method=="POST":
        form=form_class(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            return redirect(redir)
    else:
        form=form_class(instance=instance)
    return render(request,'Boutique/forms.html',{'form':form,'titre':"modification PRO"})

@permission_required('Boutique.delete_client', login_url=LOGIN_URL)
def delete(request,ob,pk,pk2):
    model_name=MODEL_NAMES.get(ob)
    permission=f'Boutique.delete_{model_name}'

    if not request.user.has_perm(permission):
        return render(request,'Boutique/403.html')
    
    if ob==0:
        obj=get_object_or_404(Client,ncli=pk)
        redir='clients'
    elif ob==1:
        obj=get_object_or_404(Commande,ncom=int(pk))
        redir='commandes'
    elif ob==2:
        obj=get_object_or_404(Detail,commande_id=int(pk),produit_id=pk2)
        redir='details'
    else:
        obj=get_object_or_404(Produit,npro=pk)
        redir='products'
    if request.method=="POST":
        obj.delete()
        return redirect(redir)
    
    return render(request,'Boutique/delete_confirm.html',{'object':obj,'type':"cet element"})





#---------Vue d'autentification
def register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('clients')
    else:
        form=RegisterForm()
    return render(request,'Boutique/auth/register.html',{'form':form})
    

def connexion(request):
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('clients')
    else:
        form=AuthenticationForm()
    return render(request,'Boutique/auth/login.html',{'form':form})

@require_POST  
def deconnexion(request):
    logout(request)
    return redirect('connexion')

@user_passes_test(est_adminstrateur,login_url=LOGIN_URL)
def tableau_bord_admin(request):

    nb_clients=Client.objects.count()
    nb_produits=Produit.objects.count()
    nb_commandes=Commande.objects.count()
    nb_details=Detail.objects.count()

    return render(request,'Boutique/admin_dashboard.html',{
        'nb_clients':nb_clients,
        'nb_produits':nb_produits,
        'nb_commandes':nb_commandes,
        'nb_details':nb_details,
    })

@login_required(login_url=LOGIN_URL)
def profile(request):
    username=request.user.username 
    email=request.user.email
    groups=request.user.groups.all()

    return render(request,"Boutique/profile.html",{
        'username':username,
        'email':email,
        'groups':groups,
    })







        


