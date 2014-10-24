# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0003_workcate_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workcate',
            options={'ordering': ['sort', '-add_time']},
        ),
        migrations.AlterModelOptions(
            name='workitem',
            options={'ordering': ['sort', '-add_time']},
        ),
    ]
