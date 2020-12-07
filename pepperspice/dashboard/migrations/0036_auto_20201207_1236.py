# Generated by Django 3.1.1 on 2020-12-07 12:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0035_auto_20201130_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertrait',
            name='aws_uid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dbnode',
            name='Date_Created',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 7, 12, 36, 54, 844803)),
        ),
        migrations.AlterField(
            model_name='deleted_node',
            name='date_deleted',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 7, 12, 36, 54, 846728)),
        ),
        migrations.AlterField(
            model_name='node',
            name='Date_Created',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 7, 12, 36, 54, 845791)),
        ),
        migrations.AlterField(
            model_name='uploadedproject',
            name='Date_Uploaded',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 7, 12, 36, 54, 842755)),
        ),
    ]