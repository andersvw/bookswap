# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150404_1556'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='authorbook',
            table='author_book',
        ),
        migrations.AlterModelTable(
            name='book',
            table='book',
        ),
    ]
