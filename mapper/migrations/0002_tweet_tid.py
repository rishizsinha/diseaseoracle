# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapper', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='tid',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
