from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Jurusan(models.Model):
    Informatika = 1
    Teknik_Komputer = 2
    Teknik_Elektro = 3
    Studi_Islam_Interdisipliner = 4
    Agribisnis = 5
    Farmasi = 6
    Pendidikan_Guru_Sekolah_Dasar = 7
    Pendidikan_Bahasa_Inggris = 8
    Menejemen = 9
    Akuntansi = 10
    Teknologi_Hasil_Pertanian = 11
    jurusan = [
        ('Informatika', 'INF'),
        ('Teknik_Komputer', 'T.KOM'),
        ('Teknik_Elektro', 'T.EL'),
        ('Studi_Islam_Interdisipliner', 'SII'),
        ('Agribisnis', 'AGR'),
        ('Farmasi', 'FAR'),
        ('Pendidikan_Guru_Sekolah_Dasar', 'PGSD'),
        ('Pendidikan_Bahasa_Inggris', 'PBI'),
        ('Menejemen', 'MNJ'),
        ('Akuntansi', 'AKT'),
        ('Teknologi_Hasil_Pertanian', 'THP'),
    ]
    
    jurusan = models.CharField(choices=jurusan, default=True, max_length=30)

    def __str__(self):
        return self.jurusan


class User(AbstractUser):
    jurusan = models.CharField(max_length=30)
    is_panitia = models.BooleanField('Panitia', default=False)
    is_pemilih = models.BooleanField('Pemilih', default=False)
    # jurusan = models.ForeignKey(Jurusan, on_delete=models.CASCADE, related_name='bagian',blank=True, null=True)


# class Users(AbstractUser):
#     jurusan = [
#         ('Informatika', 'INF'),
#         ('Teknik Komputer', 'T.KOM'),
#         ('Teknik Elektro', 'T.EL'),
#         ('Studi Islam Interdisipliner', 'SII'),
#         ('Agribisnis', 'AGR'),
#         ('Farmasi', 'FAR'),
#         ('Pendidikan Guru Sekolah Dasar', 'PGSD'),
#         ('Pendidikan Bahasa Inggris', 'PBI'),
#         ('Menejemen', 'MNJ'),
#         ('Akuntansi', 'AKT'),
#         ('Teknologi Hasil Pertanian', 'THP'),
#     ]
#     REQUIRED_FIELDS = ('owner', 'group')
    
#     owner = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owners')
#     group = models.OneToOneField(Group, on_delete=models.CASCADE, related_name='groups')
#     jurusan = models.CharField(choices=jurusan, default='', max_length=30, blank=True, null=True)