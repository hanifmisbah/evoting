from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.http import urlencode

# from .encrypt import encryptData, decryptData

from panitia import models as panitiamodels
from .models import Vote

# Create your views here.
# @login_required(login_url='/account/login')
def index(req):
    agenda = panitiamodels.Agenda.objects.filter(status='aktif').values()
    return render(req, 'pemilih/index.html', {
        'data' : agenda,
    })

def showdatakandidat(req, id):
    if req.method == 'GET':
        showdetail= panitiamodels.Agenda.objects.filter(pk=id).first()
        detailbyid = showdetail.agenda.all()
        
        return render(req, 'pemilih/voting.html', {
            'data' : detailbyid,
            # 'detail' : showdetail,
        })

def vote(req, id):
    get_kandidat = panitiamodels.Kandidat.objects.get(pk=id)
    vote = Vote.objects.create(kandidat=get_kandidat)
    print(vote)
    messages.success(req, f'Vote Berhasil')
    return redirect('/pemilih')
    
    