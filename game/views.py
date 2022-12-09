from django.shortcuts import get_object_or_404, render #A privilegier
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Match, Ligue, Equipe

class IndexView(generic.ListView):
    template_name = 'game/index.html'
    context_object_name = 'latest_equipe_list'
    def get_queryset(self):
        """Return the teams sorted by score."""
        return sorted(Equipe.objects.all(), key = lambda p: p.score)

class EquipeView(generic.DetailView):
    model = Equipe
    template_name = 'game/detail.html'

class ResultsView(generic.DetailView):
    model = Match
    template_name = 'game/results.html'