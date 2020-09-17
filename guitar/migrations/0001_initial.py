# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutGuitar',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=60)),
                ('overview', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='guitar', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Batches',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('batch_name', models.CharField(max_length=60)),
                ('batch_datetime', models.DateTimeField()),
                ('days', models.CharField(max_length=15, choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')])),
                ('details', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Buyguitar',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=60)),
                ('amount', models.CharField(max_length=60)),
                ('details', models.CharField(max_length=60)),
                ('overview', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='guitar', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feestructure',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('Programmes_name', models.CharField(max_length=50)),
                ('Days_per_week', models.CharField(max_length=50)),
                ('Class_duration', models.CharField(max_length=50)),
                ('fees', models.CharField(max_length=50)),
                ('certification', models.CharField(max_length=15, choices=[('Yes', 'Yes'), ('No', 'No')])),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='YoutubeVideos',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=60)),
                ('link', models.CharField(max_length=300)),
            ],
        ),
    ]
