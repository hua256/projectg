# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-10 00:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('grumblee', '0011_auto_20180706_0131'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeIngredients',
            fields=[
                ('guid', models.CharField(default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('quantity', models.PositiveIntegerField()),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grumblee.Ingredient')),
            ],
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='ingredients',
        ),
        migrations.AlterField(
            model_name='day',
            name='recipes',
            field=models.ManyToManyField(blank=True, to='grumblee.Recipe'),
        ),
        migrations.AddField(
            model_name='recipeingredients',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grumblee.Recipe'),
        ),
    ]
