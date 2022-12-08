from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
#1-Participant
#2-Matchs


class Equipe(models.Model):
    # ID= models.IntegerField(default=0)
    nom = models.CharField(max_length=70)
    # prenom = models.CharField(max_length=70)
    classement= models.IntegerField(default=0)
    def __str__(self):
        return self.nom

class Ligue(models.Model):
    # ID = models.IntegerField(default=0)
    nom = models.CharField(max_length=70,default="")
    def __str__(self):
        return self.nom

# class Equipe:
#     ID: int #PK
#     nom: str
#     joueurs: Participant[]

class Match(models.Model):
    # ID = models.IntegerField(default=0)
    nom = models.CharField(max_length=70,default="match")
    date = models.DateTimeField('date du match',default=datetime.datetime(2022, 12, 8, 8, 11, 9, 493056, tzinfo=datetime.timezone.utc))
    locaux= models.ForeignKey(Equipe, on_delete=models.CASCADE,default="",related_name="locaux") #ou Equipe si matchs entre equipes
    visiteur =models.ForeignKey(Equipe, on_delete=models.CASCADE,default="",related_name="visiteur") #ou Equipe si matchs entre equipes
    ligue = models.ForeignKey(Ligue, on_delete=models.CASCADE, default="")
    score = models.CharField(default="0-0",max_length=5)
    def __str__(self):
        return self.nom

# class Set:
#     score1: 
#     score2: