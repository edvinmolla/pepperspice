# Generated by Django 2.1.15 on 2020-08-05 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_dbnode_db_port'),
    ]

    operations = [
        migrations.AddField(
            model_name='dbnode',
            name='db_password',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='dbnode',
            name='db_username',
            field=models.CharField(default='', max_length=128),
        ),
    ]
