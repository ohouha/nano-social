# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-22 03:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialnetwork', '0018_auto_20160221_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='mypro',
            field=models.ForeignKey(blank=True, db_column='pro', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='socialnetwork.profile'),
        ),
    ]
