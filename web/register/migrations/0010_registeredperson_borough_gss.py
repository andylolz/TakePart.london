# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0009_auto_20160526_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeredperson',
            name='borough_gss',
            field=models.CharField(blank=True, db_index=True, max_length=100),
        ),
    ]
