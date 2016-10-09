# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0003_auto_20161001_2309'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='spammessage',
            options={'ordering': ['date_posted']},
        ),
        migrations.RemoveField(
            model_name='spammessage',
            name='date_created',
        ),
        migrations.AddField(
            model_name='profile',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date profile created'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user_bio',
            field=models.CharField(max_length=500, blank=True),
        ),
        migrations.AddField(
            model_name='spammessage',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date posted'),
        ),
    ]
