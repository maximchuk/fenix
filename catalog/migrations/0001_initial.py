# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-06 01:02
from __future__ import unicode_literals

import catalog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.ImageField(upload_to='media/cover', verbose_name='Постер')),
                ('date_add', models.DateTimeField(verbose_name='Дата')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('description', models.TextField(max_length=300, verbose_name='Описание')),
                ('is_open', models.BooleanField(help_text='Дать доступ к файлу для всех пользователей', verbose_name='Для всех')),
                ('is_slug', models.BooleanField(help_text='Файл будет доступет только по ссылке', verbose_name='По ссылке')),
                ('is_for_me', models.BooleanField(help_text='Файл будет доступен только Вам', verbose_name='Только для меня')),
            ],
            options={
                'verbose_name': 'Файл',
                'db_table': 'catalog',
                'verbose_name_plural': 'Файлы',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Категория',
                'db_table': 'category',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files_s', models.FileField(upload_to=catalog.models.upload_file, verbose_name='Файл')),
                ('slug', models.SlugField()),
                ('catalog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Catalog')),
            ],
            options={
                'verbose_name': 'Файл',
                'db_table': 'files',
                'verbose_name_plural': 'Файлы',
            },
        ),
        migrations.AddField(
            model_name='catalog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='catalog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
    ]
