# Generated by Django 2.2.13 on 2020-10-03 08:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backManage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 3, 8, 24, 29, 459933, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 3, 8, 24, 29, 462939, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='member',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 3, 8, 24, 29, 465968, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='team',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 3, 8, 24, 29, 468971, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='team',
            name='work_id',
            field=models.CharField(max_length=10, unique=True, verbose_name='项目编号'),
        ),
        migrations.AlterField(
            model_name='work',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 3, 8, 24, 29, 474977, tzinfo=utc)),
        ),
    ]
