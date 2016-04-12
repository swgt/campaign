# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-12 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voters', '0003_auto_20160412_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='cityVoting',
            field=models.CharField(default='São Gonçalo do Amarante', max_length=50, verbose_name='Cidade do Local de Votação'),
        ),
        migrations.AddField(
            model_name='person',
            name='districtVoting',
            field=models.CharField(default='padrao', max_length=50, verbose_name='Bairro do Local de Votação'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='localNameVoting',
            field=models.CharField(default='padrao', max_length=50, verbose_name='Nome do Local de Votação'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='numberVoting',
            field=models.CharField(default='padrao', max_length=6, verbose_name='Número do Local de Votação'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='stateVoting',
            field=models.CharField(default='RN', max_length=2, verbose_name='Estado do Local de Votação'),
        ),
        migrations.AddField(
            model_name='person',
            name='streetVoting',
            field=models.CharField(default='padrao', max_length=50, verbose_name='Rua do Local de Votação'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='whatsapp',
            field=models.CharField(default='padrap', max_length=15, verbose_name='whatsapp'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, max_length=50, verbose_name='email'),
        ),
    ]
