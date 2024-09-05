
from django.db import models
import uuid

class Menu(models.Model):
    # id est une chaîne de caractères unique, on utilise UUID pour garantir l'unicité
    id = models.CharField(max_length=36, default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    
    # creation_date est un champ de type Date
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Menu {self.id} créé le {self.creation_date}"
