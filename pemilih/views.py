from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.http import urlencode

from panitia.models import *
from .models import *

from .forms import *

# Create your views here.
def index(req, year=datetime.now().year):
    polls = Poll.objects.all().values()
    try:
        agenda = Agenda.objects.filter(owner__jurusan=req.user.jurusan, waktu_awal__year=year, status='aktif').values()
    except:
        return redirect('/')
    return render(req, 'pemilih/index.html', {
        'data' : agenda,
        'polls' : polls,
    })


def select_agenda(req, agenda_id):
    agenda = Agenda.objects.get(pk=agenda_id)
    agenda_id = Poll.objects.create(owner=req.user, agenda=agenda)
    return redirect('aggrement')    


def aggrement(req):
    agenda = Poll.objects.order_by('-id')[:1]
    return render(req, 'pemilih/aggrement.html',{
        'agenda':agenda,
    })


def cancel_agenda(req, agenda_id):
    Poll.objects.filter(owner=req.user, pk=agenda_id).delete()
    return redirect('/pemilih')


def polls(req, id):
    polls = Poll.objects.get(pk=id)
    filter_agenda = polls.agenda
    kandidat = filter_agenda.agenda.all()
    print(kandidat)
    
    return render(req, 'pemilih/voting.html',{
        'kandidat':kandidat,
        'agenda':filter_agenda,
        'id':id,
    })
    

def buat_vote(req, agenda_id, id):
    kandidats = Kandidat.objects.get(pk=id)
    buat_pilihan = Poll.objects.filter(owner=req.user, pk=agenda_id).update(kandidat=kandidats)
    return redirect('/pemilih')
    
    
    
    
    
    
    
    
    
    