# Generated by Django 3.2.11 on 2022-06-16 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=26, unique=True)),
                ('waktu_awal', models.DateTimeField(blank=True, null=True)),
                ('waktu_akhir', models.DateTimeField(blank=True, null=True)),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Kandidat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=26)),
                ('jk', models.CharField(choices=[('Laki-Laki', 'Laki-Laki'), ('Perempuan', 'Perempuan')], default='Laki-Laki', max_length=9)),
                ('jurusan', models.CharField(choices=[('Informatika', 'INF'), ('Teknik Komputer', 'T.KOM'), ('Teknik Elektro', 'T.EL')], default='INF', max_length=26)),
                ('nim', models.PositiveBigIntegerField(max_length=9, unique=True)),
                ('tgl_lahir', models.DateField(verbose_name=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y'])),
                ('tpt_lahir', models.CharField(max_length=26)),
                ('no_wa', models.PositiveBigIntegerField(default=0, max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('visi', models.TextField()),
                ('misi', models.TextField()),
                ('agenda', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='termasuk', to='panitia.agenda')),
            ],
        ),
    ]
