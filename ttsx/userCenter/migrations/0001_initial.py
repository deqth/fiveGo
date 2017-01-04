# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='address_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tel', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('zipcode', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=50)),
                ('isDelete', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.IntegerField()),
                ('goods_info', models.ForeignKey(to='shopping.GoodsInfo')),
            ],
            options={
                'db_table': 'cart',
            },
        ),
        migrations.CreateModel(
            name='OrderDetailInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bpub_date', models.DateTimeField()),
                ('ordernum', models.CharField(max_length=20)),
                ('goods_price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('count', models.DecimalField(max_digits=5, decimal_places=2)),
                ('goods', models.ForeignKey(to='shopping.GoodsInfo')),
            ],
            options={
                'db_table': 'OrderDetailInfo',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.BooleanField()),
                ('total', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
            options={
                'db_table': 'OrderInfo',
            },
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=20)),
                ('passwd', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='user',
            field=models.ForeignKey(to='userCenter.user'),
        ),
        migrations.AddField(
            model_name='orderdetailinfo',
            name='order',
            field=models.ForeignKey(to='userCenter.OrderInfo'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(to='userCenter.user'),
        ),
        migrations.AddField(
            model_name='address_info',
            name='user',
            field=models.ForeignKey(to='userCenter.user'),
        ),
    ]
