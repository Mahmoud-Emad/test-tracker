# Generated by Django 4.0.4 on 2022-05-24 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("test_tracker", "0013_remove_testcases_unique_testcase_title_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="REQ_TC_Title",
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]
