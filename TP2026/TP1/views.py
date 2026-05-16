from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,"SUB/dashboard.html")

def about(request):
    return HttpResponse("approps de nous")

def catalogue(request):
    context={
        "magasine":"marjane",
    }
    return render(request,"SUB/catalogue.html",context)

