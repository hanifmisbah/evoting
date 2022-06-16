from django.shortcuts import render, redirect

from panitia import models as panitiamodels
from .models import Vote

# Create your views here.

def index(request):
    kandidat = panitiamodels.Kandidat.objects.all()
    print(kandidat)
    return render(request, 'voting.html', {'kandidat': kandidat})

def vote_2(request, kandidat_id, agenda_id):
    # judul = panitiamodels.judul.objects.all()
    agendabyid = panitiamodels.Agenda.objects.get(pk=agenda_id)
    # kandidatbyid = panitiamodels.Kandidat.objects.get(pk=kandidat_id)
    Vote.objects.create(kandidat=agenda_id)
    # messages.info(request, f'yeeeeeeeeeeeeha, hakdes hakdeds | Vote Berhasil | uhuyyyyy josss')
    return redirect('/')
