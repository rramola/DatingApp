# Generated by Django 5.0.3 on 2024-05-28 02:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0017_alter_datingprofile_gender_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="datingprofile",
            name="gender",
            field=models.CharField(
                choices=[("Male", "MALE"), ("Femal", "FEMALE")],
                max_length=50,
                null=True,
            ),
        ),
    ]
