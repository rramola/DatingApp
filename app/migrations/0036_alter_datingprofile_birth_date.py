# Generated by Django 5.0.3 on 2024-06-04 04:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0035_remove_datingprofile_age_datingprofile_birth_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="datingprofile",
            name="birth_date",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
