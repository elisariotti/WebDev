# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-08-07 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20180806_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='subscriber',
        ),
        migrations.AddField(
            model_name='profile',
            name='newsletter_reader',
            field=models.NullBooleanField(default=True, help_text='Select yes if you want to receive our newsletters.'),
        ),
    ]
