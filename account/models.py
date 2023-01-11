from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Jurusan(models.Model):
    kode = models.PositiveBigIntegerField(default=0)
    jurusan = models.CharField(default='', max_length=30)
        
    def __str__(self):
        return self.jurusan
    
    def toDict(self):
        return {
            'id': self.id,
            'kode': self.kode,
            'jurusan': self.jurusan,
        }



class User(AbstractUser):
    jurusan = models.ForeignKey(Jurusan, on_delete=models.CASCADE, related_name='kodes', null=True, blank=True)
    nim = models.PositiveBigIntegerField(unique=True, null=True)
    no_wa = models.PositiveBigIntegerField(null=True)
    is_panitia = models.BooleanField('Panitia', default=False)
    is_pemilih = models.BooleanField('Pemilih', default=False)
    
    def toDict(self):
        return {
            'id': self.id,
            'jurusan': self.jurusan.toDict(),
            'nim': self.nim,
            'no_wa': self.no_wa,
            'is_panitia': self.is_panitia,
            'is_pemilih': self.is_pemilih,
        }
