# Generated by Django 3.2.11 on 2022-12-13 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panitia', '0006_kandidat_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kandidat',
            name='foto',
            field=models.ImageField(default='img/icon.png', upload_to='images/'),
        ),
    ]
