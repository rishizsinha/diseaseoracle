# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField()),
                ('text', models.CharField(max_length=150)),
                ('geo', models.CharField(max_length=150)),
                ('coordinates', models.CommaSeparatedIntegerField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('user_tz', models.CharField(max_length=100)),
                ('lang', models.CharField(max_length=10)),
            ],
        ),
    ]
