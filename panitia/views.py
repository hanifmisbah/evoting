from django.shortcuts import render, redirect
from django.contrib import messages

from . import models
from .forms import KandidatForm, PemilihanForm

# Create your views here.
def index(req):
    agenda = models.Agenda.objects.all()
    return render(req, 'panitia/index.html', {
        'data' : agenda,
    })

def base(req):
    return render(req, 'base1.html')

def cari(req):
    if req.POST:
        cari = req.POST['cari']
        return render(req, 'panitia/index.html', {
            'cari' : cari,
        })
    else:
        return render(req, 'panitia/index.html', {

        })

def agenda(req):
    agenda = models.Agenda.objects.order_by('-id')
    return render(req, 'panitia/agenda.html', {
        'data' : agenda,
    })

def tambah_agenda(req):
    form = PemilihanForm()
    if req.POST:
        agenda = models.Agenda.objects.create(
          judul = req.POST['judul'],  
          waktu_awal = req.POST['waktu_awal'],  
          waktu_akhir = req.POST['waktu_akhir'],  
        #   durasi = req.POST['durasi'],  
        )
        form = PemilihanForm(req.POST)
        if form.is_valid():
            form.save()
        return redirect('/agenda')
    pemilihan = models.Agenda.objects.all()
    return render(req, 'panitia/tambah_agenda.html', {
        'data' : pemilihan,
        'form' : form,
    })

def agenda_update(req, id):
    if req.POST:
        agenda = models.Agenda.objects.filter(pk=id).update(
          judul = req.POST['judul'],  
          waktu_awal = req.POST['waktu_awal'],  
          waktu_akhir = req.POST['waktu_akhir'],  
        #   durasi = req.POST['durasi'],  
        )
        messages.info(req, f'Edit berhasil')
        return redirect('/agenda')
    pemilihan = models.Agenda.objects.filter(pk=id).first()
    return render(req, 'panitia/edit_agenda.html', {
        'data' : pemilihan,
    })

def agenda_delete(req, id):
    hapus = models.Agenda.objects.filter(pk=id).delete()
    # messages.info(req, f'{hapus.judul} berhasil dihapus')
    return redirect('/agenda')



def list_kandidat(req):
    kandidat = models.Kandidat.objects.order_by('-id')
    return render(req, 'panitia/list_kandidat.html', {
        'data' : kandidat,
    })

def kandidat(req):
    form = KandidatForm()
    if req.POST:
        kandidat = models.Kandidat.objects.create(
            nama = req.POST['nama'],
            nim = req.POST['nim'],
            tgl_lahir = req.POST['tgl_lahir'],
            tpt_lahir = req.POST['tpt_lahir'],
            no_wa = req.POST['no_wa'],
            email = req.POST['email'],
            visi = req.POST['visi'],
            misi = req.POST['misi'],
        )
        form = KandidatForm(req.POST)
        if form.is_valid():
            form.save()
        return redirect('/list_kandidat')
    kandidat = models.Kandidat.objects.all()
    return render(req, 'panitia/kandidat.html', {
        'data' : kandidat,
        'form' : form,
    })
def kandidat_delete(req, id):
    hapus = models.Kandidat.objects.filter(pk=id).delete()
    # messages.info(req, f'{hapus.judul} berhasil dihapus')
    return redirect('/kandidat')