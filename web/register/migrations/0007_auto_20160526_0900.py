# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0006_auto_20160525_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeredperson',
            name='postcode',
            field=models.CharField(blank=True, db_index=True, max_length=100),
        ),
    ]