# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-26 03:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qaProgram', '0005_auto_20170826_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graddetail',
            name='avatar',
            field=models.ImageField(default='d', upload_to='img'),
            preserve_default=False,
        ),
    ]