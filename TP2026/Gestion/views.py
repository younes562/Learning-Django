from django.http import HttpResponse

def dashboard_admin(request):
    return HttpResponse("Bienvenue dans l'espace administrateur")
