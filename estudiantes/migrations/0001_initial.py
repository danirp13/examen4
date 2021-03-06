# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 04:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('nombres', models.CharField(blank=True, max_length=100)),
                ('apellidos', models.CharField(blank=True, max_length=100)),
                ('direccion', models.CharField(blank=True, max_length=200)),
                ('fecha_nac', models.DateField()),
                ('observaciones', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('descripcion', models.CharField(blank=True, max_length=100)),
                ('profesor', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='estudiante',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiantes.Materia'),
        ),
    ]
