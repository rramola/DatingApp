# Generated by Django 5.0.3 on 2024-05-29 00:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0021_alter_personalityprofile_are_you_active_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="first_name",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="last_name",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
