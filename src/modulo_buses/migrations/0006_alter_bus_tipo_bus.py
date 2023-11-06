# Generated by Django 4.2.6 on 2023-11-04 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_buses', '0005_remove_bus_capacidad_remove_bus_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='tipo_bus',
            field=models.CharField(blank=True, choices=[('Microbus', 'Microbus'), ('Coaster', 'Coaster')], max_length=256, verbose_name='Tipo de Autobus'),
        ),
    ]