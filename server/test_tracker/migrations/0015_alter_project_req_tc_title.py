# Generated by Django 4.0.4 on 2022-05-24 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("test_tracker", "0014_alter_project_req_tc_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="REQ_TC_Title",
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]
