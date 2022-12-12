import datetime

from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class AddMatchForm(forms.Form):
    datematch = forms.DateField(
        help_text="Enter a date between now and 4 weeks (default 3)."
        )
    nom_match = forms.CharField(
        help_text="Nom du Match"
    )

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
