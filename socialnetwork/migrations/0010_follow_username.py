# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-14 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialnetwork', '0009_auto_20160214_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='follow',
            name='username',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]