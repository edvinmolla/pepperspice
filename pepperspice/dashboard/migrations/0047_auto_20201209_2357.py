# Generated by Django 3.1.1 on 2020-12-09 23:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0046_auto_20201209_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api_service',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 9, 23, 57, 59, 364562)),
        ),
        migrations.AlterField(
            model_name='dbnode',
            name='Date_Created',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 9, 23, 57, 59, 366096)),
        ),
        migrations.AlterField(
            model_name='deleted_node',
            name='date_deleted',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 9, 23, 57, 59, 367951)),
        ),
        migrations.AlterField(
            model_name='node',
            name='Date_Created',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 9, 23, 57, 59, 367086)),
        ),
        migrations.AlterField(
            model_name='uploadedproject',
            name='Date_Uploaded',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 9, 23, 57, 59, 363424)),
        ),
    ]
