from django.shortcuts import render, redirect

from panitia import models as panitiamodels
from .models import Vote

# Create your views here.

def index(req):
    a = panitiamodels.Agenda.objects.filter(status='aktif').values()
    return render(req, 'pemilih/index.html', {
        'data' : a,
    })
    
def showdatakandidat(req, id):
    if req.method == 'GET':
        showdetail= panitiamodels.Agenda.objects.filter(pk=id).first()
        detailbyid = showdetail.agenda.all()
        
        return render(req, 'pemilih/voting.html', {
            'data' : detailbyid,
        })

def vote(req, id):
    vote = panitiamodels.Kandidat.objects.get(pk=id)
    Vote.objects.create(
        kandidat=vote
        )
    
    return redirect('/pemilih')
    # messages.info(request, f'yeeeeeeeeeeeeha, hakdes hakdeds | Vote Berhasil | uhuyyyyy josss')
    
    
    