# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-07-03 02:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=25)),
                ('ApellidoPaterno', models.CharField(max_length=25)),
                ('ApellidoMaterno', models.CharField(max_length=25)),
                ('Correo', models.CharField(max_length=40)),
                ('DNI', models.CharField(max_length=8)),
                ('Telefono', models.CharField(max_length=9)),
                ('Cargo', models.CharField(max_length=25)),
                ('FechaIngreso', models.DateField()),
                ('Foto', models.ImageField(upload_to='Photo')),
            ],
        ),
    ]
