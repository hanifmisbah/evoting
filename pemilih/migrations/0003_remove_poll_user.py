# Generated by Django 3.2.11 on 2022-11-30 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pemilih', '0002_poll'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='user',
        ),
    ]
