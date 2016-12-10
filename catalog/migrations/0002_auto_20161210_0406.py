# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-10 02:06
from __future__ import unicode_literals

import catalog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filescatalog',
            name='files_s',
            field=models.FileField(upload_to=catalog.models.upload_file, verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='filesexpres',
            name='files_s',
            field=models.FileField(upload_to=catalog.models.upload_file, verbose_name='Файл'),
        ),
        migrations.AlterModelTable(
            name='filesexpres',
            table='files_expres',
        ),
    ]