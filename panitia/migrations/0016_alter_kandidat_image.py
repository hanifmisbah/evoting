# Generated by Django 3.2.11 on 2023-01-11 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panitia', '0015_alter_kandidat_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kandidat',
            name='image',
            field=models.ImageField(blank=True, default='../static/img/dlf.pt-password-icon-png-4816679.png', upload_to='images/'),
        ),
    ]
