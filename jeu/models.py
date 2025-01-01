from django.db import models

class Question(models.Model):
    id = models.IntegerField(primary_key=True)  # ID de la question
    texte = models.CharField(max_length=255)  # Texte de la question
    attribut = models.CharField(max_length=100)  # Attribut cible (ex. "homme")

    def __str__(self):
        return self.texte

class Personnage(models.Model):
    nom = models.CharField(max_length=255)  # Nom du personnage
    attributs = models.JSONField()  # Attributs

    def __str__(self):
        return self.nom
