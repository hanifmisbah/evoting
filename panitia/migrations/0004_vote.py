# Generated by Django 3.2.11 on 2022-07-06 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('panitia', '0003_alter_kandidat_tgl_lahir'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saat', to='panitia.agenda')),
                ('kandidat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sesuai', to='panitia.kandidat')),
            ],
        ),
    ]