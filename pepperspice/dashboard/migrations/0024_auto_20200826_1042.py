# Generated by Django 3.0.7 on 2020-08-26 10:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0023_auto_20200826_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedproject',
            name='file_uuid',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='dbnode',
            name='Date_Created',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 26, 10, 42, 55, 25997)),
        ),
        migrations.AlterField(
            model_name='deleted_node',
            name='date_deleted',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 26, 10, 42, 55, 29055)),
        ),
        migrations.AlterField(
            model_name='node',
            name='Date_Created',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 26, 10, 42, 55, 27531)),
        ),
        migrations.AlterField(
            model_name='uploadedproject',
            name='Date_Uploaded',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 26, 10, 42, 55, 19850)),
        ),
    ]
