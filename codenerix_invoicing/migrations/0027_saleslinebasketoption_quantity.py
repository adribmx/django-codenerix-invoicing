# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-03 18:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codenerix_invoicing', '0026_auto_20170803_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleslinebasketoption',
            name='quantity',
            field=models.FloatField(default=1, verbose_name='Quantity'),
            preserve_default=False,
        ),
    ]
