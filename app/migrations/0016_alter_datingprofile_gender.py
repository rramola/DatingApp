# Generated by Django 5.0.3 on 2024-05-28 01:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0015_rename_userprofile_profile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="datingprofile",
            name="gender",
            field=models.CharField(
                choices=[("MALE", "1"), ("FEMALE", "2")], max_length=50, null=True
            ),
        ),
    ]