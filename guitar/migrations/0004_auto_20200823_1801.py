# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guitar', '0003_auto_20200823_1041'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='Mobie',
            new_name='Mobile',
        ),
    ]
