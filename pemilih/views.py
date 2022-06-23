from django.shortcuts import render, redirect

from panitia import models as panitiamodels
from .models import Vote

# Create your views here.

def index(req, id):
    if req.method == 'GET':
        agenda = panitiamodels.Agenda.objects.filter(pk=id).first()
        print(agenda)
        detailbyid = agenda.termasuk.all()

        showbyagenda = []
        for s in detailbyid:
            showbyagenda.append(s)
            print(showbyagenda)
            return render(req, 'pemilih/index.html', {'datadetail': showbyagenda})
    else:
        return render(req, 'pemilih/index.html')
        
def vote_2(request, kandidat_id, agenda_id):
    agendabyid = panitiamodels.Agenda.objects.get(pk=agenda_id)
    Vote.objects.create(kandidat=agenda_id)
    # messages.info(request, f'yeeeeeeeeeeeeha, hakdes hakdeds | Vote Berhasil | uhuyyyyy josss')
    return redirect('/')
