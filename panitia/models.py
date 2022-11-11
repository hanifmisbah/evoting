from distutils.command.install_egg_info import to_filename
from email.policy import default
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Agenda(models.Model):
    status = [
        ('aktif', 'aktif'),
        ('tidak aktif', 'tidak aktif'),
    ]

    judul = models.CharField(unique=True, max_length=100)
    waktu_awal = models.DateTimeField(blank=True, null=True)
    waktu_akhir = models.DateTimeField(blank=True, null=True)
    status = models.CharField(default='', choices=status, max_length=11)
    # durasi = models.TimeField(blank=True)

    def __str__(self):
        return self.judul

class Jurusan(models.Model):
    jurusan = [
        ('Informatika', 1),
        ('Teknik Komputer', 2),
        ('Teknik Elektro', 3),
        ('Studi Islam Interdisipliner', 4),
        ('Agribisnis', 5),
        ('Farmasi', 6),
        ('Pendidikan Guru Sekolah Dasar', 7),
        ('Pendidikan Bahasa Inggris', 8),
        ('Menejemen', 9),
        ('Akuntansi', 10),
        ('Teknologi Hasil Pertanian', 11),
    ]
    
    jurusan = models.CharField(choices=jurusan, default='INF', max_length=30)

    def __str__(self):
        return self.jurusan

class Kandidat(models.Model):
    jenis_kelamin = [
        ('Laki-Laki', 'Laki-Laki'),
        ('Perempuan', 'Perempuan'),
    ]

    # input_formats = ['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y']

    # foto = models.ImageField(null=True, blank=True, upload_to='images/')
    nama = models.CharField(max_length=26)
    jurusan = models.ForeignKey(Jurusan, on_delete=models.CASCADE, related_name='bagian',blank=True, null=True)
    jk = models.CharField(default='Laki-Laki', choices=jenis_kelamin, max_length=9)
    domisili = models.CharField(default='', max_length=50)
    nim = models.PositiveBigIntegerField(unique=True)
    tgl_lahir = models.DateField()
    tpt_lahir = models.CharField(max_length=26)
    no_wa = models.PositiveBigIntegerField(default=0)
    email = models.EmailField()
    visi = RichTextField(blank=True, null=True)
    misi = RichTextField(blank=True, null=True)
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE, related_name='agenda',blank=True, null=True)
    # vote = models.PositiveBigIntegerField(default=0, max_length=100)

    def __str__(self):
        return self.nama

    def result(self):
        return self.vote + 1