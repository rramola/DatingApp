# Generated by Django 5.0.3 on 2024-06-04 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_alter_personalityprofile_hobby_pick_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalityprofile',
            name='what_do_you_do_for_fun_pick',
            field=models.CharField(choices=[('Hiking', 'HIKING'), ('Gaming', 'GAMING'), ('Reading', 'READING'), ('Singing', 'SINGING'), ('Sports', 'SPORTS'), ('Dancing', 'DANCING'), ('Travel', 'TRAVEL')], max_length=300, null=True),
        ),
    ]
