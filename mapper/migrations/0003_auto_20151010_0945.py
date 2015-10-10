# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapper', '0002_tweet_tid'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='within1mo',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tweet',
            name='within1wk',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tweet',
            name='within2wk',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
