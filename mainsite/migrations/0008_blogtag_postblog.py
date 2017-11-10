# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 10:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0007_auto_20171109_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogTag',
            fields=[
                ('uid', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PostBlog',
            fields=[
                ('uid', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('tags', models.ManyToManyField(related_name='postblog_blogtag', to='mainsite.BlogTag')),
            ],
        ),
    ]