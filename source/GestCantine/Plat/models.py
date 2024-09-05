from django.db import models
import uuid

class Plat(models.Model):
    # id est une chaîne de caractères unique, on utilise UUID pour garantir l'unicité
    id = models.CharField(max_length=36, default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    
    # name est un champ de texte pour le nom du plat
    name = models.CharField(max_length=255)
    
    # summary est un champ texte plus long pour une description sommaire du plat
    summary = models.TextField()

    def __str__(self):
        return self.name
