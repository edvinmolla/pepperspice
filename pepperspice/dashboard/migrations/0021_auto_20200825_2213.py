# Generated by Django 3.0.7 on 2020-08-25 22:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0020_auto_20200825_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedproject',
            name='file_type',
            field=models.CharField(default='', max_length=16),
        ),
        migrations.AlterField(
            model_name='dbnode',
            name='Date_Created',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 25, 22, 13, 51, 45589)),
        ),
        migrations.AlterField(
            model_name='deleted_node',
            name='date_deleted',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 25, 22, 13, 51, 47216)),
        ),
        migrations.AlterField(
            model_name='node',
            name='Date_Created',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 25, 22, 13, 51, 46387)),
        ),
        migrations.AlterField(
            model_name='uploadedproject',
            name='Date_Uploaded',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 25, 22, 13, 51, 41938)),
        ),
    ]
