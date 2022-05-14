# Generated by Django 4.0.4 on 2022-05-13 15:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_tracker', '0007_remove_project_people_people_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='email',
        ),
        migrations.RemoveField(
            model_name='people',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='people',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='people',
            name='user',
        ),
        migrations.AddField(
            model_name='people',
            name='host_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='host_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='people',
            name='invited_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='invited_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
