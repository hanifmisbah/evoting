# Generated by Django 3.2.11 on 2022-12-09 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pemilih', '0010_alter_poll_kandidat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='kandidat',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
