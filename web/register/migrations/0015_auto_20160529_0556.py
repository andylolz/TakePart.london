# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 05:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0014_llsoa'),
    ]

    operations = [
        migrations.AddField(
            model_name='borough',
            name='population_2014',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='borough',
            name='population_voting_age_2014',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='borough',
            name='population_young_2014',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='llsoa',
            name='population_2014',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='llsoa',
            name='population_voting_age_2014',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='llsoa',
            name='population_young_2014',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ward',
            name='population_2014',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ward',
            name='population_voting_age_2014',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ward',
            name='population_young_2014',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
