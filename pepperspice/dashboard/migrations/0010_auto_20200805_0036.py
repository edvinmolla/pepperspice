# Generated by Django 2.1.15 on 2020-08-05 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_node_server_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='link_status',
            field=models.BooleanField(default=False),
        ),
    ]
