from django.db import models
from django.utils import timezone
import datetime

class Equipe(models.Model):
    nom = models.CharField(max_length=70)
    ligues = models.ManyToManyField('Ligue')
        
    @property
    def score(self):
        match =  Match.objects.filter(locaux__id__exact=self.id)|Match.objects.filter(visiteur__id__exact=self.id)
        score = 0
        for matches in match:
            if (not matches.score_locaux ) or (not matches.score_visiteurs ):
                continue
            elif matches.locaux.id==self.id:
                if matches.score_locaux > matches.score_visiteurs:score+=3
                elif matches.score_locaux < matches.score_visiteurs:score-=0
                elif matches.score_locaux == matches.score_visiteurs:score+=1
                else: print("SYSTEM ERROR")
            elif matches.visiteur.id==self.id:
                if matches.score_locaux < matches.score_visiteurs:score+=3
                elif matches.score_locaux > matches.score_visiteurs:score-=0
                elif matches.score_locaux == matches.score_visiteurs:score+=1
                else: print("SYSTEM ERROR")
            else: print("SYSTEM ERROR")
        return score
    
    @property
    def matches(self):
        return Match.objects.filter(locaux__id__exact=self.id)|Match.objects.filter(visiteur__id__exact=self.id)

    def __str__(self):
        return self.nom


class Ligue(models.Model):
    nom = models.CharField(max_length=70,default="")
    
    @property
    def equipes(self):
        equipe_set = set()
        for equipe in Equipe.objects.all():
            for ligue in equipe.ligues.all():
                if ligue.id == self.id:
                    equipe_set.add(equipe)
        return equipe_set  

    def __str__(self):
        return self.nom
  

class Match(models.Model):
    nom = models.CharField(max_length=70,default="")
    date = models.DateTimeField('date du match',default=datetime.datetime(2022, 12, 8, 8, 11, 9, 493056, tzinfo=datetime.timezone.utc))
    locaux= models.ForeignKey(Equipe, on_delete=models.CASCADE,default="",related_name="locaux") #ou Equipe si matchs entre equipes
    visiteur =models.ForeignKey(Equipe, on_delete=models.CASCADE,default="",related_name="visiteur") #ou Equipe si matchs entre equipes
    ligue = models.ForeignKey(Ligue, on_delete=models.CASCADE, default="")
    score_locaux = models.IntegerField(null=True, blank=True)
    score_visiteurs = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.nom
