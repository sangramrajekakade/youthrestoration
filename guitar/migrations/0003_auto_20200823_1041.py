# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guitar', '0002_appointment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='Name',
            new_name='F_Name',
        ),
        migrations.AddField(
            model_name='appointment',
            name='L_Name',
            field=models.CharField(max_length=200, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='Mobie',
            field=models.CharField(max_length=200, default=1),
            preserve_default=False,
        ),
    ]
