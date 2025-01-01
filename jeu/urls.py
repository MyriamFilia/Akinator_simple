# jeu/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.accueil, name="accueil"),
    path("theme/", views.theme, name="theme"),
    path("jeu/personnages/", views.jeu_akinator, {"theme": "personnages"}, name="jeu_personnages"),
    path("jeu/objets/", views.jeu_akinator, {"theme": "objets"}, name="jeu_objets"),
    path("jeu/animaux/", views.jeu_akinator, {"theme": "animaux"}, name="jeu_animaux"),
    path("jeu/<str:theme>/", views.jeu_akinator, name="jeu_akinator"),
    path("reinitialiser/", views.reinitialiser, name="reinitialiser"),
]
