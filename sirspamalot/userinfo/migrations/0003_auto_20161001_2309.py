# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userinfo', '0002_auto_20161001_2116'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpamMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date created')),
                ('spam_message', models.CharField(max_length=140)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date_created'],
            },
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='interaction',
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
