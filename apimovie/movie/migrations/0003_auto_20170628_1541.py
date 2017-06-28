# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 15:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_film'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('release_date', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('synopsis', models.CharField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='film',
            name='date',
        ),
        migrations.AddField(
            model_name='description',
            name='film',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='movie.Film'),
        ),
    ]
