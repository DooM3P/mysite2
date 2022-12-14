from django.shortcuts import get_object_or_404, render #A privilegier
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from game.forms import add_match_form, modify_matchForm
import datetime


from .models import Match, Ligue, Equipe

class EquipesView(generic.ListView):
    template_name = 'game/class_equipes.html'
    context_object_name = 'equipe_list'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ligue'] = Ligue.objects.get(id=self.kwargs['ligue_id'])
        context['matches'] = sorted(Match.objects.filter(ligue=self.kwargs['ligue_id']), key = lambda p: p.nom,reverse=0)
        return context

    def get_queryset(self):
        """Return the teams sorted by score."""
        for i in Equipe.objects.filter(ligues=self.kwargs['ligue_id']):
            i.score2 = i.score(self.kwargs['ligue_id'])
            i.save()
        return sorted(Equipe.objects.filter(ligues=self.kwargs['ligue_id']),key = lambda p : p.score(self.kwargs['ligue_id']), reverse=1)
    

class EquipeView(generic.DetailView):
    model = Equipe
    template_name = 'game/detail.html'


class LigueView(generic.ListView):
    template_name = 'game/index.html'
    context_object_name = 'ligue_list'
    def get_queryset(self):
        """Return the teams sorted by score."""
        return sorted(Ligue.objects.all(), key = lambda p: p.nom)

def add_match(request):
    match = Match(nom="Match de Test", locaux=Equipe.objects.get(id=1), visiteur=Equipe.objects.get(id=2),ligue=Ligue(nom = "Ligue Internationale"),)
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = add_match_form(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            match = Match(nom=form.clean_nom_match(),
                date=form.clean_datematch(),
                locaux=form.clean_locaux(), visiteur=form.clean_visiteur(),
                ligue=form.clean_ligue(), score_locaux=form.clean_score_locaux(),
                score_visiteurs=form.clean_score_visiteurs()
            ) 
            match.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('game:ligues'))

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_datematch = datetime.date.today() 
        form = add_match_form(initial={'datematch': proposed_datematch,
            'score_locaux': 0,
            'score_visiteurs':0
        }
        )

    context = {
        'form': form,
        'match': match,
    }

    return render(request, 'game/add_match.html', context)

def create_matches(request, ligue_id):
    equipes = Equipe.objects.filter(ligues=ligue_id)
    for i in equipes:
        equipes = equipes.exclude(id=i.id)
        for j in equipes:
            if Match.objects.filter(locaux=i,visiteur=j,ligue=Ligue.objects.get(id=ligue_id)).count() == 0:
                Match(nom="Test", locaux=i, visiteur=j, ligue=Ligue.objects.get(id=ligue_id)).save()
            if Match.objects.filter(locaux=j,visiteur=i,ligue=Ligue.objects.get(id=ligue_id)).count() == 0:
                Match(nom="Test", locaux=j, visiteur=i, ligue=Ligue.objects.get(id=ligue_id)).save()
    return HttpResponseRedirect(reverse('game:class_equipes',kwargs={'ligue_id': ligue_id}))

def modify_match(request, match_id):
    match = Match.objects.get(id=match_id)
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = modify_matchForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            match.date=form.clean_datematch()
            match.score_locaux=form.clean_score_locaux()
            match.score_visiteurs=form.clean_score_visiteurs()
            match.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('game:ligues'))

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_datematch = datetime.date.today() 
        form = modify_matchForm(initial={'datematch': proposed_datematch,
            'score_locaux': 0,
            'score_visiteurs':0
        }
        )

    context = {
        'form': form,
        'match': match,
    }

    return render(request, 'game/modify_match.html', context)