# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 17:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_comedien'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comedien',
            name='films',
        ),
        migrations.AddField(
            model_name='comedien',
            name='film',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.Film'),
        ),
    ]
