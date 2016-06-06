# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-06 18:23
from __future__ import unicode_literals
from django.db import migrations
from stats.models import BattingAvg


def add_data(apps, schema_editor):
    BattingAvg.objects.create(name='Manny Machado', position='CF', games=2, at_bats=4, runs=6, hits=6, doubles=4,
                              triples=5, home_runs=5, rbi=9, strike_outs=4, average=.400)


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_data)
    ]
