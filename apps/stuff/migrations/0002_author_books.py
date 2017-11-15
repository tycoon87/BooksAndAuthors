# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 03:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='Authors', to='stuff.Book'),
        ),
    ]
