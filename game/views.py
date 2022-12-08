from django.shortcuts import get_object_or_404, render #A privilegier
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Match, Ligue, Equipe

class IndexView(generic.ListView):
    template_name = 'game/index.html'
    context_object_name = 'latest_equipe_list'
    def get_queryset(self):
        """Return the last five published questions."""
        return Equipe.objects.order_by('nom')[:5]


class EquipeView(generic.DetailView):
    model = Equipe
    template_name = 'game/detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["match_list"] = Match.objects.filter(locaux__id__exact=context['object'].id)|Match.objects.filter(visiteur__id__exact=context['object'].id)
        return context

class ResultsView(generic.DetailView):
    model = Match
    template_name = 'game/results.html'