# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-06 01:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grumblee', '0009_auto_20180706_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groceryitem',
            name='week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grumblee.Week'),
        ),
    ]
