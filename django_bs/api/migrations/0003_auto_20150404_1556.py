# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150404_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'db_table': 'college',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('abbreviation', models.CharField(max_length=4)),
                ('number', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'course',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CourseBook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'course_book',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('book_condition', models.CharField(max_length=100, null=True, blank=True)),
                ('description', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'db_table': 'listing',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=44)),
                ('salt', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50, null=True, blank=True)),
                ('last_name', models.CharField(max_length=50, null=True, blank=True)),
                ('email', models.CharField(max_length=50, null=True, blank=True)),
                ('address', models.CharField(max_length=150, null=True, blank=True)),
                ('phone_number', models.CharField(max_length=10, null=True, blank=True)),
            ],
            options={
                'db_table': 'user_info',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='authorbook',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'managed': False},
        ),
    ]
