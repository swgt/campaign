# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-26 02:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voters', '0003_auto_20160525_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='veiculo',
            field=models.BooleanField(default=False, verbose_name='Vai precisar de Veículo?'),
        ),
        migrations.AlterField(
            model_name='person',
            name='dataNascimento',
            field=models.DateField(verbose_name='Data de Nascimento'),
        ),
    ]
