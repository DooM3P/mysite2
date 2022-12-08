from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render #A privilegier
from django.template import loader
from django.http import Http404

from .models import Match, Ligue, Equipe

def index(request):
    latest_equipe_list = Equipe.objects.order_by('nom')[:5]
    # template = loader.get_template('game/index.html')
    context = {
        'latest_equipe_list': latest_equipe_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'game/index.html', context)

def detail(request, equipe_id):
    equipe = get_object_or_404(Equipe, pk=equipe_id)
    match_list = Match.objects.filter(locaux__id__exact=equipe_id)|Match.objects.filter(visiteur__id__exact=equipe_id)
    context = {
        'equipe': equipe,
        'match_list': match_list,
    }
    return render(request, 'game/detail.html', context)
    # try:
    #     equipe = Equipe.objects.get(pk=equipe_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'game/detail.html', {'equipe': equipe})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)