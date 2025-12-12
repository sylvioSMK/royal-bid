from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenue dans l'application Enchère !")
