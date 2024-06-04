# Generated by Django 5.0.3 on 2024-06-03 23:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0031_alter_datingprofile_profile_pic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="personalityprofile",
            name="hobby_pick",
            field=models.CharField(
                choices=[
                    ("Biking", "BIKING"),
                    ("Knitting", "KNITTING"),
                    ("Painting", "PAINTING"),
                    ("Bird-watching", "BIRD-WATCHING"),
                    ("Antiquing", "ANTIQUING"),
                    ("Couch-Potato", "COUCH-POTATO"),
                    ("Kayaking", "KAYAKING"),
                    ("Swimming", "SWIMMING"),
                ],
                max_length=300,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="personalityprofile",
            name="interests",
            field=models.CharField(
                choices=[
                    ("Long-term", "Long-term partner"),
                    ("Short-term", "Short-term partner"),
                    ("Firguring-out", "Still figuring out"),
                ],
                max_length=50,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="personalityprofile",
            name="movie_pick",
            field=models.CharField(
                choices=[
                    ("Horror", "HORROR"),
                    ("Romance", "ROMANCE"),
                    ("Comedy", "COMEDY"),
                    ("Action", "ACTION"),
                    ("Anime", "ANIME"),
                    ("Sci-fi", "SCI-FI"),
                ],
                max_length=300,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="personalityprofile",
            name="music_pick",
            field=models.CharField(
                choices=[
                    ("Metal", "METAL"),
                    ("Classic", "CLASSIC"),
                    ("Country", "COUNTRY"),
                    ("Pop", "POP"),
                    ("Hip-hop", "HIP-HOP"),
                    ("Gospel", "GOSPEL"),
                ],
                max_length=300,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="personalityprofile",
            name="outdoor_indoor_pick",
            field=models.CharField(
                choices=[("Outdoor", "OUTDOOR"), ("Indoor", "INDOOR")],
                max_length=50,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="personalityprofile",
            name="sport_pick",
            field=models.CharField(
                choices=[
                    ("Baseball", "BASEBALL"),
                    ("Basketball", "BASKETBALL"),
                    ("Tennis", "TENNIS"),
                    ("Football", "FOOTBALL"),
                    ("Soccer", "SOCCER"),
                    ("Skate", "SKATING"),
                    ("Golf", "GOLF"),
                ],
                max_length=300,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="personalityprofile",
            name="what_do_you_do_for_fun_pick",
            field=models.CharField(
                choices=[
                    ("Hiking", "HIKING"),
                    ("Gaming", "GAMING"),
                    ("Reading", "READING"),
                    ("Singing", "SINGING"),
                    ("Sports", "SPORTS"),
                    ("Dancing", "DANCING"),
                    ("Travel", "TRAVEL"),
                    ("Poetry", "POETRY"),
                    ("Music", "MUSIC"),
                ],
                max_length=300,
                null=True,
            ),
        ),
    ]