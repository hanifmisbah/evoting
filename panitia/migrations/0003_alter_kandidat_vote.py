# Generated by Django 3.2.11 on 2022-10-28 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panitia', '0002_kandidat_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kandidat',
            name='vote',
            field=models.BigIntegerField(default=0, max_length=100),
        ),
    ]