# Generated by Django 2.2.13 on 2020-10-04 11:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backManage', '0018_auto_20201004_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='password',
        ),
        migrations.AlterField(
            model_name='college',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 4, 11, 36, 46, 400649, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 4, 11, 36, 46, 402649, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='member',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 4, 11, 36, 46, 405629, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='team',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 4, 11, 36, 46, 408634, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='work',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 4, 11, 36, 46, 413639, tzinfo=utc)),
        ),
    ]
