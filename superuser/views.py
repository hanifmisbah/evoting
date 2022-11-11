from django.shortcuts import render, redirect

from panitia.models import * 

from panitia.forms import *
from account.forms import *
# Create your views here.
def index(req):
    return render(req, 'superadmin/index.html')

def agenda(req):
    agenda_vote = Agenda.objects.order_by('-id')
    return render(req, 'superadmin/agenda.html', {
        'data' : agenda_vote,
    })

def tambah_agenda(req):
    form = PemilihanForm()
    if req.POST:
        form = PemilihanForm(req.POST)
        if form.is_valid():
            form.save()
            print(form)
        return redirect('agenda')
    pemilihan = Agenda.objects.all()
    return render(req, 'superadmin/tambah-agenda.html', {
        'data' : pemilihan,
        'form' : form,
    })


def kandidat(req):
    kandidat = Kandidat.objects.order_by('-id')
    return render(req, 'superadmin/kandidat.html', {
        'data' : kandidat,
    })

def tambah_kandidat(req):
    form = KandidatForm()
    if req.POST:
        form = KandidatForm(req.POST)
        if form.is_valid():
            form.save()
        return redirect('list_kandidat')
    return render(req, 'superadmin/tambah-kandidat.html', {
        'form' : form,
    })

def tambah_panitia(req):
    form = RegisForm()
    if req.POST:
        form = RegisForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return redirect('/')
            
    return render(req, 'superadmin/tambah-panitia.html', {
        'form':form,
    })