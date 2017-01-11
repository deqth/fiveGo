# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='address_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('receiver', models.CharField(max_length=15, verbose_name=b'\xe6\x94\xb6\xe4\xbb\xb6\xe4\xba\xba')),
                ('tel', models.CharField(max_length=15, verbose_name=b'\xe7\x94\xb5\xe8\xaf\x9d\xe5\x8f\xb7\xe7\xa0\x81')),
                ('email', models.EmailField(max_length=254, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1')),
                ('zipcode', models.CharField(max_length=10, verbose_name=b'\xe9\x82\xae\xe7\xbc\x96')),
                ('address', models.CharField(max_length=50, verbose_name=b'\xe5\x9c\xb0\xe5\x9d\x80')),
                ('isDelete', models.BooleanField(default=0)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'address_info',
                'verbose_name': '\u5730\u5740\u4fe1\u606f',
                'verbose_name_plural': '\u5730\u5740\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.IntegerField(verbose_name=b'\xe6\x95\xb0\xe9\x87\x8f')),
                ('isselect', models.BooleanField()),
                ('goods_info', models.ForeignKey(to='shopping.GoodsInfo')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'cart',
                'verbose_name': '\u8d2d\u7269\u8f66',
                'verbose_name_plural': '\u8d2d\u7269\u8f66',
            },
        ),
        migrations.CreateModel(
            name='OrderDetailInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goods_price', models.DecimalField(verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe4\xbb\xb7\xe6\xa0\xbc', max_digits=5, decimal_places=2)),
                ('count', models.DecimalField(verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe6\x95\xb0\xe9\x87\x8f', max_digits=5, decimal_places=2)),
                ('goods', models.ForeignKey(to='shopping.GoodsInfo')),
            ],
            options={
                'db_table': 'OrderDetailInfo',
                'verbose_name': '\u8ba2\u5355\u8be6\u60c5',
                'verbose_name_plural': '\u8ba2\u5355\u8be6\u60c5',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.BooleanField(verbose_name=b'\xe6\x94\xaf\xe4\xbb\x98\xe7\x8a\xb6\xe6\x80\x81')),
                ('total', models.DecimalField(verbose_name=b'\xe6\x94\xaf\xe4\xbb\x98\xe9\x87\x91\xe9\xa2\x9d', max_digits=5, decimal_places=2)),
                ('ordernum', models.CharField(max_length=20, verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe5\x8f\xb7')),
                ('bpub_date', models.DateTimeField(verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe6\x97\xa5\xe6\x9c\x9f')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'OrderInfo',
                'verbose_name': '\u8ba2\u5355',
                'verbose_name_plural': '\u8ba2\u5355',
            },
        ),
        migrations.AddField(
            model_name='orderdetailinfo',
            name='order',
            field=models.ForeignKey(to='userCenter.OrderInfo'),
        ),
    ]
