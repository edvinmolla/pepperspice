# Generated by Django 3.1.1 on 2020-12-13 11:34

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0052_auto_20201213_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api_service',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 13, 11, 34, 45, 285971)),
        ),
        migrations.AlterField(
            model_name='credit_card',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 13, 11, 34, 45, 284164)),
        ),
        migrations.AlterField(
            model_name='dbnode',
            name='Date_Created',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 13, 11, 34, 45, 287568)),
        ),
        migrations.AlterField(
            model_name='deleted_node',
            name='date_deleted',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 13, 11, 34, 45, 289451)),
        ),
        migrations.AlterField(
            model_name='node',
            name='Date_Created',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 13, 11, 34, 45, 288532)),
        ),
        migrations.AlterField(
            model_name='uploadedproject',
            name='Date_Uploaded',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 13, 11, 34, 45, 284902)),
        ),
        migrations.CreateModel(
            name='transaction_messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_email', models.EmailField(default='', max_length=254)),
                ('message', models.CharField(default='', max_length=200)),
                ('date_created', models.DateTimeField(default=datetime.datetime(2020, 12, 13, 11, 34, 45, 283684))),
                ('user_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
