# Generated by Django 2.1.15 on 2020-08-11 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_usertrait_dbms_enabled'),
    ]

    operations = [
        migrations.AddField(
            model_name='dbnode',
            name='db_external_ip',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='dbnode',
            name='db_internal_ip',
            field=models.CharField(default='', max_length=64),
        ),
    ]
