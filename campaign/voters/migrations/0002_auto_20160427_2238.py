# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-28 01:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voters', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='cityVoting',
        ),
        migrations.RemoveField(
            model_name='person',
            name='number',
        ),
        migrations.RemoveField(
            model_name='person',
            name='numberVoting',
        ),
        migrations.RemoveField(
            model_name='person',
            name='stateVoting',
        ),
        migrations.RemoveField(
            model_name='person',
            name='streetVoting',
        ),
        migrations.AlterField(
            model_name='person',
            name='cellphone',
            field=models.CharField(blank=True, max_length=15, verbose_name='celular'),
        ),
        migrations.AlterField(
            model_name='person',
            name='whatsapp',
            field=models.CharField(blank=True, max_length=15, verbose_name='whatsapp'),
        ),
    ]
