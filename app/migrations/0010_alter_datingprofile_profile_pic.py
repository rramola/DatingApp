# Generated by Django 5.0.3 on 2024-05-27 18:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0009_alter_datingprofile_user_profile_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="datingprofile",
            name="profile_pic",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
