# Generated by Django 2.1.11 on 2020-09-20 12:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0032_auto_20200920_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dbnode',
            name='Date_Created',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 20, 12, 56, 51, 39294)),
        ),
        migrations.AlterField(
            model_name='deleted_node',
            name='date_deleted',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 20, 12, 56, 51, 41104)),
        ),
        migrations.AlterField(
            model_name='node',
            name='Date_Created',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 20, 12, 56, 51, 40218)),
        ),
        migrations.AlterField(
            model_name='uploadedproject',
            name='Date_Uploaded',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 20, 12, 56, 51, 37253)),
        ),
    ]
