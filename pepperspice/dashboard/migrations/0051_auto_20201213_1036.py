# Generated by Django 3.1.1 on 2020-12-13 10:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0050_auto_20201213_0804'),
    ]

    operations = [
        migrations.AddField(
            model_name='credit_card',
            name='issuer',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='api_service',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 13, 10, 36, 44, 779266)),
        ),
        migrations.AlterField(
            model_name='credit_card',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 13, 10, 36, 44, 777472)),
        ),
        migrations.AlterField(
            model_name='dbnode',
            name='Date_Created',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 13, 10, 36, 44, 780858)),
        ),
        migrations.AlterField(
            model_name='deleted_node',
            name='date_deleted',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 13, 10, 36, 44, 782658)),
        ),
        migrations.AlterField(
            model_name='node',
            name='Date_Created',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 13, 10, 36, 44, 781792)),
        ),
        migrations.AlterField(
            model_name='uploadedproject',
            name='Date_Uploaded',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 13, 10, 36, 44, 778218)),
        ),
    ]
