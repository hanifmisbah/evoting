from django.shortcuts import render, redirect

from panitia import models as panitiamodels
from .models import Vote

# Create your views here.

def index(req):
    a = panitiamodels.Agenda.objects.filter(status='aktif').values()
    print(a)
    return render(req, 'pemilih/index.html', {
        'data' : a,
    })

def vote(req, id):
    kandidatbyid = panitiamodels.Kandidat.objects.get(pk=id)
    Vote.objects.create(
        kandidat=kandidatbyid
        )

    result = Vote.objects.all()
    # messages.info(request, f'yeeeeeeeeeeeeha, hakdes hakdeds | Vote Berhasil | uhuyyyyy josss')
    return render(req, 'pemilih/voting.html', {
        'data' : result,
    })
