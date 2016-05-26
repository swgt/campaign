# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-26 02:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('voters', '0002_auto_20160427_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='dataNascimento',
            field=models.DateField(default=datetime.datetime(2016, 5, 26, 2, 36, 5, 795987, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='sessao',
            field=models.CharField(default=0, max_length=5, verbose_name='Sessão de Votação'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='zona',
            field=models.CharField(default='51ª ZONA ELEITORAL', max_length=100, verbose_name='Zona de Votação'),
        ),
    ]