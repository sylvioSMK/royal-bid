from django.urls import path
from . import views

urlpatterns = [
    # Temporairement une URL vide juste pour éviter l'erreur
    path('', views.index, name='index'),
]
