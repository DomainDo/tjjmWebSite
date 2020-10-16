# Generated by Django 2.2.13 on 2020-10-04 00:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backManage', '0013_auto_20201004_0837'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='is_first',
            field=models.CharField(default='否', max_length=2, verbose_name='是否为第一指导老师'),
        ),
        migrations.AlterField(
            model_name='college',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 4, 0, 58, 44, 392851, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 4, 0, 58, 44, 394852, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='member',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 4, 0, 58, 44, 396854, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='team',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 4, 0, 58, 44, 398856, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='work',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 4, 0, 58, 44, 403861, tzinfo=utc)),
        ),
    ]
