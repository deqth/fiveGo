# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('unit', models.CharField(max_length=20)),
                ('smallImg', models.ImageField(upload_to=b'')),
                ('info', models.CharField(max_length=200)),
                ('info_detail', models.CharField(max_length=3000)),
                ('bigImg', models.ImageField(upload_to=b'')),
                ('cliNum', models.IntegerField(max_length=100000)),
            ],
            options={
                'db_table': 'goods',
            },
        ),
    ]
