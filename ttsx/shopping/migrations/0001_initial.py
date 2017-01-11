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

                ('title', models.CharField(max_length=20, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe4\xbf\xa1\xe6\x81\xaf')),
                ('type', models.CharField(max_length=20, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('price', models.DecimalField(verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe4\xbb\xb7\xe6\xa0\xbc', max_digits=5, decimal_places=2)),
                ('unit', models.CharField(max_length=20, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x8d\x95\xe4\xbd\x8d')),
                ('smallImg', models.ImageField(upload_to=b'', verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\xb0\x8f\xe5\x9b\xbe')),
                ('info', models.CharField(max_length=200, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe7\xae\x80\xe4\xbb\x8b')),
                ('info_detail', models.TextField(max_length=3000, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe8\xaf\xa6\xe6\x83\x85')),
                ('bigImg', models.ImageField(upload_to=b'', verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\xa4\xa7\xe5\x9b\xbe')),
                ('inventoryNum', models.IntegerField(verbose_name=b'\xe5\xba\x93\xe5\xad\x98\xe9\x87\x8f')),
                ('cliNum', models.IntegerField(verbose_name=b'\xe7\x82\xb9\xe5\x87\xbb\xe9\x87\x8f')),
            ],
            options={
                'db_table': 'goods',
                'verbose_name': '\u5546\u54c1\u4fe1\u606f',
                'verbose_name_plural': '\u5546\u54c1\u4fe1\u606f',

            },
        ),
    ]
