# Generated by Django 2.0.3 on 2018-03-20 15:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_dpto', models.CharField(max_length=70, verbose_name='Nombre del departamento')),
                ('piso', models.CharField(max_length=5)),
                ('descripcion', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Visitante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_nombre', models.CharField(max_length=40, verbose_name='Primer Nombre')),
                ('s_nombre', models.CharField(blank=True, max_length=40, null=True, verbose_name='Segundo Nombre')),
                ('p_apellido', models.CharField(max_length=40, verbose_name='Primer Apellido')),
                ('s_apellido', models.CharField(blank=True, max_length=40, null=True, verbose_name='Segundo Apellido')),
                ('cedula', models.CharField(max_length=15, verbose_name='Cedula de Identidad')),
                ('direccion', models.CharField(max_length=200, verbose_name='Dirección de Habitación')),
                ('telefono', models.CharField(max_length=11)),
                ('fecha_hora_entrada', models.DateTimeField(default=datetime.datetime.now, verbose_name='Hora de visita')),
                ('fecha_hora_salida', models.DateTimeField(blank=True, null=True, verbose_name='Hora de salida')),
                ('dpto_visita', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aplicacionPrueba.Departamento')),
            ],
        ),
    ]
