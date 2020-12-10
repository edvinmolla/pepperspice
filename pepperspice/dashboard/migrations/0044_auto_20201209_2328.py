# Generated by Django 3.1.1 on 2020-12-09 23:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0043_auto_20201209_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api_service',
            name='api_id',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='api_service',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 9, 23, 28, 20, 961554)),
        ),
        migrations.AlterField(
            model_name='dbnode',
            name='Date_Created',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 9, 23, 28, 20, 963213)),
        ),
        migrations.AlterField(
            model_name='deleted_node',
            name='date_deleted',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 9, 23, 28, 20, 965023)),
        ),
        migrations.AlterField(
            model_name='node',
            name='Date_Created',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 9, 23, 28, 20, 964191)),
        ),
        migrations.AlterField(
            model_name='uploadedproject',
            name='Date_Uploaded',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 9, 23, 28, 20, 959986)),
        ),
    ]
