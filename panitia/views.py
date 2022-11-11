from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict

from pemilih.views import vote

from panitia.models import *
from pemilih.models import Vote 
from account.models import User 
from .forms import KandidatForm, PemilihanForm

# Create your views here.
def index(req):
    today = datetime.now().date()
    kandidat = Kandidat.objects.all().order_by('-id')
    agenda = Agenda.objects.first()
    kandidat_byagenda = agenda.agenda.all()

    print(kandidat_byagenda)

    return render(req, 'panitia/index.html', {
        'kandidat' : kandidat,
        'agenda' : agenda,
        'kandidats' : kandidat_byagenda,
    })
    
def agendafilter(req):
    agenda = Agenda.objects.filter(status='aktif').values()
    
    return render(req, 'panitia/agendafilter.html', {
        'agenda':agenda,
        # 'data' : detailbyid,
    })
def kandidatfilter(req, id):
    if req.method == 'GET':
        showdetail= Agenda.objects.filter(pk=id).first()
        detailbyid = showdetail.agenda.all()
        print(showdetail)
        print(detailbyid)
    return render(req, 'panitia/kandidatfilter.html', {
        'data' : detailbyid,
    })

# @login_required(login_url='/account/login')
def cari(req):
    if req.POST:
        cari = req.POST['cari']
        return render(req, 'panitia/index.html', {
            'cari' : cari,
        })
    else:
        return render(req, 'panitia/index.html', {

        })

# @login_required(login_url='/account/login')
def agenda(req):
    agenda_vote = Agenda.objects.order_by('-id')
    return render(req, 'panitia/agenda.html', {
        'data' : agenda_vote,
    })

# @login_required(login_url='/account/login')
def tambah_agenda(req):
    form = PemilihanForm()
    if req.POST:
        form = PemilihanForm(req.POST)
        if form.is_valid():
            form.save()
            print(form)
        return redirect('agenda')
    pemilihan = Agenda.objects.all()
    return render(req, 'panitia/tambah_agenda.html', {
        'data' : pemilihan,
        'form' : form,
    })

# @login_required(login_url='/account/login')
def agenda_update(req, id):
    form = PemilihanForm()
    agenda = Agenda.objects.get(pk=id)
    form = PemilihanForm(instance=agenda)
    
    if req.POST:
        form = PemilihanForm(req.POST, instance=agenda)
        if form.is_valid():
            form.save()
            return redirect('/agenda')

    return render(req, 'panitia/tambah_agenda.html', {
        'form' : form,
    })

# @login_required(login_url='/account/login')
def agenda_delete(req, id):
    hapus = Agenda.objects.filter(pk=id).delete()
    # messages.info(req, f'{hapus.judul} berhasil dihapus')
    return redirect('/agenda')



# @login_required(login_url='/account/login')
def list_kandidat(req):
    kandidat = Kandidat.objects.order_by('-id')
    return render(req, 'panitia/list_kandidat.html', {
        'data' : kandidat,
    })

# @login_required(login_url='/account/login')
def kandidat(req):
    form = KandidatForm()
    if req.POST:
        form = KandidatForm(req.POST)
        if form.is_valid():
            form.save()
        return redirect('list_kandidat')
    return render(req, 'panitia/kandidat.html', {
        'form' : form,
    })
    
# @login_required(login_url='/account/login')
def kandidat_update(req, id):
    form = KandidatForm()
    kandidat = Kandidat.objects.get(pk=id)
    form = KandidatForm(instance=kandidat)
    
    if req.POST:
        form = KandidatForm(req.POST, instance=kandidat)
        if form.is_valid():
            form.save()
            return redirect('list_kandidat')

    return render(req, 'panitia/kandidat.html', {
        'form' : form,
    })
    
# @login_required(login_url='/account/login')
def kandidat_delete(req, id):
    hapus = Kandidat.objects.filter(pk=id).delete()
    # messages.info(req, f'{hapus.judul} berhasil dihapus')
    return redirect('/list_kandidat')