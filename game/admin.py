from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Match,Ligue,Equipe

admin.site.register(Match)
admin.site.register(Ligue)
admin.site.register(Equipe)