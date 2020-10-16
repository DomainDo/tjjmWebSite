# Generated by Django 2.2.13 on 2020-10-03 16:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backManage', '0011_auto_20201004_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 3, 16, 29, 41, 154681, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 3, 16, 29, 41, 156682, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='member',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 3, 16, 29, 41, 158664, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='team',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 3, 16, 29, 41, 161687, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='team',
            name='tele_member2',
            field=models.CharField(default='00000', max_length=11, verbose_name='成员2手机号'),
        ),
        migrations.AlterField(
            model_name='team',
            name='tele_member3',
            field=models.CharField(default='00000', max_length=11, verbose_name='成员3手机号'),
        ),
        migrations.AlterField(
            model_name='work',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 3, 16, 29, 41, 168694, tzinfo=utc)),
        ),
    ]