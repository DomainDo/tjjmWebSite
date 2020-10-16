# Generated by Django 2.2.13 on 2020-10-12 01:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backManage', '0040_auto_20201009_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='status_review_end',
            field=models.CharField(default='否', max_length=20, verbose_name='是否评分完毕'),
        ),
        migrations.AlterField(
            model_name='college',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 12, 1, 35, 3, 793941, tzinfo=utc), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 12, 1, 35, 3, 795944, tzinfo=utc), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='judge',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 12, 1, 35, 3, 808956, tzinfo=utc), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='member',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 12, 1, 35, 3, 797944, tzinfo=utc), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='team',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 12, 1, 35, 3, 800954, tzinfo=utc), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='work',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 12, 1, 35, 3, 806954, tzinfo=utc)),
        ),
    ]