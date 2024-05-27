from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class DatingProfile(models.Model):
    user_profile = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="dating_profile_user", null=True
    )
    profile_pic = models.ImageField(upload_to="", null=True, blank=True)
    gender_options = (("1", "MALE"), ("2", "FEMALE"))
    interested_in_options = ("1", "MEN"), ("2", "WOMEN"), ("3", "BOTH")
    yes_or_no_options = (("1", "YES"), ("2", "NO"))
    gender = models.CharField(max_length=50, choices=gender_options, null=True)
    age = models.IntegerField(null=True)
    interested_in = models.CharField(
        max_length=50, choices=interested_in_options, null=True
    )
    smoker = models.CharField(max_length=50, choices=yes_or_no_options, null=True)


def createdatingProfile(user_profile, profile_pic, gender, age, interested_in, smoker):
    DatingProfile.objects.create(
        user_profile=user_profile,
        profile_pic=profile_pic,
        gender=gender,
        age=age,
        interested_in=interested_in,
        smoker=smoker,
    )


class PersonalityProfile(models.Model):
    user_profile = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="personality_profile_user",
        null=True,
    )
    yes_or_no_options = (("1", "YES"), ("1", "NO"))
    what_are_you_looking_for_options = (
        ("1", "Long-term partner"),
        ("2", "Short-term partner"),
        ("3", "Still figuring out"),
    )
    music_options = (
        ("1", "METAL"),
        ("2", "CLASSIC"),
        ("3", "COUNTRY"),
        ("4", "POP"),
        ("5", "HIP-HOP"),
        ("6", "GOSPEL"),
    )
    outdoor_indoor_options = (("1", "OUTDOOR"), ("2", "INDOOR"))
    what_do_you_do_for_fun_options = (
        ("1", "HIKING"),
        ("2", "GAMING"),
        ("3", "Reading"),
        ("4", "SINGING"),
        ("5", "SPORTS"),
        ("6", "DANCING"),
        ("7", "TRAVEL"),
        ("8", "POETRY"),
    )
    movie_genre_options = (
        ("1", "HORROR"),
        ("2", "ROMANCE"),
        ("3", "COMEDY"),
        ("4", "ACTION"),
        ("5", "ANIME"),
        ("6", "SCI-FI"),
    )
    interests = models.CharField(
        max_length=50, choices=what_are_you_looking_for_options, null=True
    )
    do_you_like_drinking = models.CharField(
        max_length=50, choices=yes_or_no_options, null=True
    )
    are_you_active = models.CharField(
        max_length=50, choices=yes_or_no_options, null=True
    )
    music_pick = models.CharField(max_length=300, choices=music_options, null=True)
    outdoor_indoor_pick = models.CharField(
        max_length=50, choices=outdoor_indoor_options, null=True
    )
    what_do_you_do_for_fun_pick = models.CharField(
        max_length=300, choices=what_do_you_do_for_fun_options, null=True
    )
    movie_pick = models.CharField(
        max_length=300, choices=movie_genre_options, null=True
    )


class Message(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="sent_messages"
    )
    recipient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="received_messages", null=True
    )

    # recipient = models.ManyToManyField(
    #     UserProfile,
    #     related_name="received_messages",
    #     through="ProfileMessage",
    # )

    content = models.TextField()
    status = models.BooleanField(default=False)
    received_date = models.DateTimeField(auto_now_add=True)
    parent_message = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="replies"
    )


# class ProfileMessage(models.Model):
#     read = models.BooleanField(default=False)
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     message = models.ForeignKey(
#         Message, on_delete=models.CASCADE, related_name="profile_messages"
#     )
