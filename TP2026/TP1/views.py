from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # Cette vue utilise un template HTML
    return render(request, "SUB/dashboard.html")

def about(request):
    # Cette vue renvoie du texte brut
    return HttpResponse("A propos de nous")