import datetime

from django import forms
from game.models import Ligue, Equipe

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class add_match_form(forms.Form):
    nom_match = forms.CharField(
        help_text="Nom du Match"
    )
    datematch = forms.DateField(
        help_text="Enter a date before now"
        )
    locaux = forms.ModelChoiceField(
        queryset=Equipe.objects.all()
    )

    visiteur = forms.ModelChoiceField(
        queryset=Equipe.objects.all()
    )

    ligue = forms.ModelChoiceField(queryset=Ligue.objects.all())

    score_locaux = forms.IntegerField()
    score_visiteurs = forms.IntegerField()
    
    def clean_nom_match(self):
        data = self.cleaned_data['nom_match']

        # Remember to always return the cleaned data.
        return data
    def clean_locaux(self):
        data = self.cleaned_data['locaux']
        return data
    def clean_visiteur(self):
        data = self.cleaned_data['visiteur']
        return data
    def clean_ligue(self):
        data = self.cleaned_data['ligue']
        return data
    def clean_score_locaux(self):
        data = self.cleaned_data['score_locaux']
        if not data : data = 0
        return data
    def clean_score_visiteurs(self):
        data = self.cleaned_data['score_visiteurs']
        if not data : data = 0
        return data
    def clean_datematch(self):
        data = self.cleaned_data['datematch']
        # Check if a date is not in the past.
        if data > datetime.date.today():
            raise ValidationError(_('Date Invalide - Match pas encore joué'))

        # Remember to always return the cleaned data.
        return data

class modify_matchForm(forms.Form):
    
    datematch = forms.DateField(
        help_text="Enter a date before now"
        )

    score_locaux = forms.IntegerField()
    score_visiteurs = forms.IntegerField()
    
    def clean_score_locaux(self):
        data = self.cleaned_data['score_locaux']
        if not data : data = 0
        return data
    def clean_score_visiteurs(self):
        data = self.cleaned_data['score_visiteurs']
        if not data : data = 0
        return data
    def clean_datematch(self):
        data = self.cleaned_data['datematch']
        # Check if a date is not in the past.
        if data > datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))
        return data

