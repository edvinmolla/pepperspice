# Generated by Django 2.1.15 on 2020-08-03 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_node_framework_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='dbnode',
            name='link_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='node',
            name='link_status',
            field=models.BooleanField(default=True),
        ),
    ]
