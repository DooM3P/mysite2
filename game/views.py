# from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render #A privilegier
# from django.template import loader
# from django.http import Http404

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


class DetailView(generic.DetailView):
    model = Equipe
    template_name = 'game/detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["match_list"] = Match.objects.filter(locaux__id__exact=context['object'].id)|Match.objects.filter(visiteur__id__exact=context['object'].id)
        return context

class ResultsView(generic.DetailView):
    model = Match
    template_name = 'game/results.html'

# def index(request):
#     latest_equipe_list = Equipe.objects.order_by('nom')[:5]
#     context = {
#         'latest_equipe_list': latest_equipe_list,
#     }
#     return render(request, 'game/index.html', context)

# def detail(request, equipe_id):
#     equipe = get_object_or_404(Equipe, pk=equipe_id)
#     match_list = Match.objects.filter(locaux__id__exact=equipe_id)|Match.objects.filter(visiteur__id__exact=equipe_id)
#     context = {
#         'equipe': equipe,
#         'match_list': match_list,
#     }
#     return render(request, 'game/detail.html', context)

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)