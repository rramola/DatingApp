# Generated by Django 5.0.3 on 2024-05-26 15:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_datingprofile_personalityprofile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='datingprofile',
            name='user_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dating_profile_user', to='app.userprofile'),
        ),
        migrations.AddField(
            model_name='personalityprofile',
            name='user_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='personality_profile_user', to='app.userprofile'),
        ),
    ]