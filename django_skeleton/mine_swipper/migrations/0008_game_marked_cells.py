# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-09 17:41
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mine_swipper', '0007_auto_20180509_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='marked_cells',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None), null=True, size=None),
        ),
    ]
