import datetime

from django import forms
from game.models import Ligue, Equipe

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class AddMatchForm(forms.Form):
    nom_match = forms.CharField(
        help_text="Nom du Match"
    )
    datematch = forms.DateField(
        help_text="Enter a date between now and 4 weeks (default 3)."
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


    def clean_datematch(self):
        data = self.cleaned_data['datematch']

        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_(
                'Invalid date - renewal more than 4 weeks ahead'
                ))

        # Remember to always return the cleaned data.
        return data
