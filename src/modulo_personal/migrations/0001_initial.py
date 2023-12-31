# Generated by Django 4.2.5 on 2023-10-26 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=256, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=256, verbose_name='Apellidos')),
                ('DPI', models.CharField(max_length=14, unique=True, verbose_name='DPI(CUI)')),
                ('telefono', models.CharField(max_length=8, verbose_name='Telefono')),
                ('correo', models.EmailField(max_length=254, unique=True, verbose_name='Correo')),
            ],
        ),
    ]
