from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils.http import urlencode
from django.db.models import Count

from panitia.models import *
from panitia.forms import *
from pemilih.models import * 
from account.models import * 
from account.forms import * 

# Create your views here.
def index(req, year=datetime.now().year, month=datetime.now().month):
    result = Agenda.objects.filter(waktu_awal__year=year, owner=req.user)    
    return render(req, 'panitia/index.html',({
        'result':result,
        'user':req.session['user'],
    }))
    
def info_kandidat(req, id):
    info = Poll.objects.filter(agenda=id).annotate(dcount=Count('kandidat'))
    print(info)
    return render(req, 'panitia/info_kandidat.html', {
        'info':info,
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

def agenda(req):
    agenda_vote = Agenda.objects.filter(owner=req.user).order_by('-id')
    return render(req, 'panitia/agenda.html', {
        'data' : agenda_vote,
    })

def tambah_agenda(req):
    form = PemilihanForm()
    if req.POST:
        form = PemilihanForm(req.POST)
        if form.is_valid():
            form.instance.owner=req.user
            form.save()
            print(form)
        return redirect('agenda')
    else:
        form = PemilihanForm()
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
            form.instance.owner=req.user
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
    kandidat = Kandidat.objects.filter(owner=req.user).order_by('-id')
    return render(req, 'panitia/list_kandidat.html', {
        'data' : kandidat,
    })

# @login_required(login_url='/account/login')
def kandidat(req):
    form = KandidatForm()
    if req.POST:
        form = KandidatForm(req.POST, req.FILES)
        if form.is_valid():
            form.instance.owner=req.user
            form.save()
            img_obj = form.instance
        return redirect('list_kandidat')
    else:
        form = KandidatForm()
    return render(req, 'panitia/kandidat.html', {
        'form' : form,
        'img_obj' : img_obj,
    })
    
# @login_required(login_url='/account/login')
def kandidat_update(req, id):
    form = KandidatForm()
    kandidat = Kandidat.objects.get(pk=id)
    form = KandidatForm(instance=kandidat)
    
    if req.POST:
        form = KandidatForm(req.POST, instance=kandidat)
        if form.is_valid():
            form.instance.owner=req.user.jurusan
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

def pemilih(req):
    pemilih = User.objects.filter(jurusan=req.user.jurusan, is_pemilih=True).values()
    return render(req, 'panitia/pemilih.html', {
        'pemilih':pemilih,
    })


def regisPemilih(req):
    form = RegisForm(initial={'jurusan':req.user.jurusan})
    print(form)
    if req.POST:
        form = RegisForm(req.POST)
        if form.is_valid():
            form.instance.owner=req.user.jurusan
            form.save()
            return redirect('data_pemilih')
    return render(req, 'panitia/regisPemilih.html', {'form':form,})



