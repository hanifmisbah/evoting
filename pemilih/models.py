from django.db import models
from panitia import models as panitia_models

# Create your models here.
class Vote(models.Model):
    agenda = models.ForeignKey(panitia_models.Agenda, on_delete=models.CASCADE, related_name='memilih', blank=True, null=True)

    # def __str__(self):
    #     return self.kandidat.nama