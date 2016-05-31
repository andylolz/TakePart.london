# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0008_postcodecachedata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postcodecachedata',
            name='id',
        ),
        migrations.AlterField(
            model_name='postcodecachedata',
            name='postcode',
            field=models.CharField(blank=True, max_length=100, primary_key=True, serialize=False),
        ),
    ]