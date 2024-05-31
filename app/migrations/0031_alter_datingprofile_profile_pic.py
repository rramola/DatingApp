from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0030_alter_datingprofile_profile_pic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="datingprofile",
            name="profile_pic",
            field=models.ImageField(
                blank=True, default="default_pic.jpg", null=True, upload_to=""
            ),
        ),
    ]
