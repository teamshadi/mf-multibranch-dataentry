# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-13 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_auto_20171013_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='securitybond',
            name='deposit_place',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='securityfutures',
            name='deposit_place',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='securityoption',
            name='deposit_place',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='securityshare',
            name='deposit_place',
            field=models.CharField(max_length=10),
        ),
        migrations.DeleteModel(
            name='DepositPlace',
        ),
    ]
