# Generated by Django 3.1.1 on 2020-12-15 03:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0053_auto_20201213_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='credit_card',
            name='card_company',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='api_service',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 15, 3, 3, 53, 356920)),
        ),
        migrations.AlterField(
            model_name='credit_card',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 15, 3, 3, 53, 355260)),
        ),
        migrations.AlterField(
            model_name='dbnode',
            name='Date_Created',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 15, 3, 3, 53, 358429)),
        ),
        migrations.AlterField(
            model_name='deleted_node',
            name='date_deleted',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 15, 3, 3, 53, 360207)),
        ),
        migrations.AlterField(
            model_name='node',
            name='Date_Created',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 15, 3, 3, 53, 359333)),
        ),
        migrations.AlterField(
            model_name='transaction_messages',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 15, 3, 3, 53, 354693)),
        ),
        migrations.AlterField(
            model_name='uploadedproject',
            name='Date_Uploaded',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 15, 3, 3, 53, 355913)),
        ),
    ]
