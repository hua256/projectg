# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-20 02:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grumblee', '0013_day_week'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='defaultQuantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='pluCode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
