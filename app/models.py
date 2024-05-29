from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(null=True, max_length=255)
    last_name = models.CharField(null=True, max_length=255)
    has_dating_profile = models.BooleanField(default=False)


class DatingProfile(models.Model):
    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="dating_profile_user",
        null=True,
    )
    created = models.BooleanField(default=False)
    profile_pic = models.ImageField(
        default="no-profile-picture-icon-15_oLIFS4i.jpg",
        null=True,
        blank=True,
    )
    gender_options = (("Male", "MALE"), ("Female", "FEMALE"))
    interested_in_options = ("Men", "MEN"), ("Women", "WOMEN"), ("Both", "BOTH")
    yes_or_no_options = (("Yes", "YES"), ("No", "NO"))
    gender = models.CharField(max_length=50, choices=gender_options, null=True)
    age = models.IntegerField(null=True)
    interested_in = models.CharField(
        max_length=50, choices=interested_in_options, null=True
    )
    smoker = models.CharField(max_length=50, choices=yes_or_no_options, null=True)


# def createdatingProfile(user_profile, profile_pic, gender, age, interested_in, smoker):
#     DatingProfile.objects.create(
#         user_profile=user_profile,
#         profile_pic=profile_pic,
#         gender=gender,
#         age=age,
#         interested_in=interested_in,
#         smoker=smoker,
#     )


class PersonalityProfile(models.Model):
    user_profile = models.ForeignKey(
        DatingProfile,
        on_delete=models.CASCADE,
        related_name="dating_profile_user",
        null=True,
    )
    created = models.BooleanField(default=False)
    yes_or_no_options = (("Yes", "YES"), ("No", "NO"))
    what_are_you_looking_for_options = (
        ("long-term", "Long-term partner"),
        ("short-term", "Short-term partner"),
        ("firguring-out", "Still figuring out"),
    )
    music_options = (
        ("metal", "METAL"),
        ("classic", "CLASSIC"),
        ("country", "COUNTRY"),
        ("pop", "POP"),
        ("hip-hop", "HIP-HOP"),
        ("gospel", "GOSPEL"),
    )
    outdoor_indoor_options = (("outdoor", "OUTDOOR"), ("indoor", "INDOOR"))
    what_do_you_do_for_fun_options = (
        ("hiking", "HIKING"),
        ("gaming", "GAMING"),
        ("reading", "Reading"),
        ("singing", "SINGING"),
        ("sport", "SPORTS"),
        ("dancing", "DANCING"),
        ("travel", "TRAVEL"),
        ("poetry", "POETRY"),
    )
    movie_genre_options = (
        ("horror", "HORROR"),
        ("romance", "ROMANCE"),
        ("comedy", "COMEDY"),
        ("action", "ACTION"),
        ("anime", "ANIME"),
        ("sci-fi", "SCI-FI"),
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
        Profile, on_delete=models.CASCADE, null=True, related_name="sent_messages"
    )
    recipient = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="received_messages", null=True
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
