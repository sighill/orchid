# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-08 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orchidee',
            name='img',
            field=models.ImageField(default='static/mainsite/img/orchidee/orchidee_default.png', help_text="Essayer de recadrer l'image pour qu'elle soit le plus \t\tcarrée possible. Si pas d'image fournie, une image par défaut est prévue.", upload_to='static/mainsite/img/orchidee/'),
        ),
    ]
