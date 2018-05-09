# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-09 04:52
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rows', models.IntegerField(default=10, validators=[django.core.validators.MaxValueValidator(30), django.core.validators.MinValueValidator(10)])),
                ('columns', models.IntegerField(default=10, validators=[django.core.validators.MaxValueValidator(30), django.core.validators.MinValueValidator(10)])),
                ('mines_count', models.IntegerField(default=10, validators=[django.core.validators.MaxValueValidator(30), django.core.validators.MinValueValidator(10)])),
                ('mines_left', models.IntegerField(default=0)),
                ('cells', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(), size=None), size=None)),
                ('flags', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(), size=None), size=None)),
                ('status', models.IntegerField(choices=[(1, 'Started'), (2, 'Paused'), (3, 'Lost'), (4, 'Won')], default=10)),
                ('seconds', models.IntegerField(default=0)),
                ('started_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_turn', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='last_move', to=settings.AUTH_USER_MODEL)),
                ('payers', models.ManyToManyField(related_name='games', to=settings.AUTH_USER_MODEL)),
                ('turn', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_move', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]