# Generated by Django 4.0.4 on 2022-06-18 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_tracker', '0027_alter_testplan_temps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testplan',
            name='temps',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]
