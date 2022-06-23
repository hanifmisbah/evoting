from django.db import models

# Create your models here.
class Agenda(models.Model):
    judul = models.CharField(unique=True, max_length=26)
    waktu_awal = models.DateTimeField(blank=True, null=True)
    waktu_akhir = models.DateTimeField(blank=True, null=True)
    # status = models.BooleanField()
    # durasi = models.TimeField(blank=True)

    def __str__(self):
        return self.judul


class Kandidat(models.Model):
    jurusan = [
        ('Informatika', 'INF'),
        ('Teknik Komputer', 'T.KOM'),
        ('Teknik Elektro', 'T.EL'),
    ]
    jenis_kelamin = [
        ('Laki-Laki', 'Laki-Laki'),
        ('Perempuan', 'Perempuan'),
    ]

    input_formats = ['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y']

    nama = models.CharField(max_length=26)
    jk = models.CharField(default='Laki-Laki', choices=jenis_kelamin, max_length=9)
    jurusan = models.CharField(default='INF', choices=jurusan, max_length=26)
    nim = models.PositiveBigIntegerField(unique=True)
    tgl_lahir = models.DateField(input_formats)
    tpt_lahir = models.CharField(max_length=26)
    no_wa = models.PositiveBigIntegerField(default=0)
    email = models.EmailField()
    visi = models.TextField(blank=False)
    misi = models.TextField(blank=False)
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE, related_name='termasuk', blank=True, null=True)

    def __str__(self):
        return self.nama
