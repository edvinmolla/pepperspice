# Generated by Django 2.1.15 on 2020-08-05 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_auto_20200805_0112'),
    ]

    operations = [
        migrations.AddField(
            model_name='dbnode',
            name='db_port',
            field=models.IntegerField(default=0),
        ),
    ]
