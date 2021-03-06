# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_auto_20160525_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='borough',
            name='population_voting_age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='borough',
            name='population_young',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ward',
            name='population_voting_age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ward',
            name='population_young',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
