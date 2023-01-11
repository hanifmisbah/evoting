from django.db import models
from panitia.models import *
from account.models import *

# Create your models here.
class Vote(models.Model):
    kandidat = models.ForeignKey(Kandidat, on_delete=models.CASCADE, related_name='memilih', blank=True, null=True)

    def __str__(self):
        return self.kandidat.nama
        
        
class Poll(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pemilih_vote', blank=True, null=True)
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE, related_name='agendas', blank=True, null=True)
    kandidat = models.ForeignKey(Kandidat, on_delete=models.CASCADE, related_name='pilih', blank=True, null=True)

    def __str__(self):
        return self.agenda.judul

