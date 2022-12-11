from django.shortcuts import get_object_or_404, render #A privilegier
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from game.forms import AddMatchForm
import datetime


from .models import Match, Ligue, Equipe

class IndexView(generic.ListView):
    template_name = 'game/index.html'
    context_object_name = 'equipe_list'
    def get_queryset(self):
        """Return the teams sorted by score."""
        return sorted(Equipe.objects.all(), key = lambda p: p.score,reverse=1)

class EquipeView(generic.DetailView):
    model = Equipe
    template_name = 'game/detail.html'

class LigueView(generic.ListView):
    template_name = 'game/ligue.html'
    context_object_name = 'ligue_list'
    def get_queryset(self):
        """Return the teams sorted by score."""
        return sorted(Ligue.objects.all(), key = lambda p: p.nom,reverse=0)

class ResultsView(generic.DetailView):
    model = Match
    template_name = 'game/results.html'

def AddMatch(request#, pk
):
    # book_instance = get_object_or_404(BookInstance, pk=pk)
    match = Match(nom="Match de Test", locaux=Equipe.objects.get(id=1), visiteur=Equipe.objects.get(id=2),ligue=Ligue(nom = "Ligue Internationale"), score_locaux=3, score_visiteurs=7 )
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = AddMatchForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            match = Match(nom="Match de Test",
                date=form.cleaned_data['renewal_date'],
                locaux=Equipe.objects.get(id=1), visiteur=Equipe.objects.get(id=2),ligue=Ligue(id=1), score_locaux=3, score_visiteurs=7
            ) 
            match.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('index'))

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = AddMatchForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'match': match,
    }

    return render(request, 'game/add_match.html', context)