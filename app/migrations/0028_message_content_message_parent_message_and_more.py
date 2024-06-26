# Generated by Django 5.0.3 on 2024-05-29 02:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0027_remove_message_content_remove_message_parent_message_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="content",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="message",
            name="parent_message",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="replies",
                to="app.message",
            ),
        ),
        migrations.AddField(
            model_name="message",
            name="received_date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="message",
            name="status",
            field=models.BooleanField(default=False, null=True),
        ),
    ]
