# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-12 14:16
from __future__ import unicode_literals

import callcenter.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callcenter', '0005_auto_20170312_0045'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appel',
            options={'get_latest_by': 'id'},
        ),
        migrations.AlterField(
            model_name='userextend',
            name='first_call_of_the_day',
            field=models.DateTimeField(blank=True, default=callcenter.models.get_default_date),
        ),
    ]
