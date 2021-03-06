# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 13:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeredperson',
            name='address_hash',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='registeredperson',
            name='borough',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='register.Borough'),
        ),
        migrations.AlterField(
            model_name='registeredperson',
            name='ward',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='register.Ward'),
        ),
    ]
