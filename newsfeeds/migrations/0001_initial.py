# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('code', models.IntegerField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('tag', models.CharField(max_length=100)),
                ('heading', models.CharField(null=True, blank=True, max_length=100)),
                ('body', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('link', models.CharField(max_length=200)),
                ('image_url', models.CharField(null=True, blank=True, max_length=500)),
                ('country', models.ForeignKey(to='newsfeeds.Country')),
            ],
        ),
    ]
