# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 00:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenter', '0006_auto_20170312_1416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appel',
            name='user',
        ),
        migrations.DeleteModel(
            name='PrecomputeData',
        ),
        migrations.DeleteModel(
            name='Appel',
        ),
    ]