from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(null=True, max_length=255)
    last_name = models.CharField(null=True, max_length=255)


class DatingProfile(models.Model):
    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="dating_profile_user",
        null=True,
    )
    created = models.BooleanField(default=False)
    profile_pic = models.ImageField(
        default="default_pic.jpg",
        null=True,
        blank=True,
    )
    gender_options = (("Male", "MALE"), ("Female", "FEMALE"))
    interested_in_options = ("Men", "MEN"), ("Women", "WOMEN"), ("Both", "BOTH")
    yes_or_no_options = (("Yes", "YES"), ("No", "NO"))
    gender = models.CharField(max_length=50, choices=gender_options, null=True)
    birth_date = models.DateTimeField(default=datetime.now)
    interested_in = models.CharField(
        max_length=50, choices=interested_in_options, null=True
    )
    smoker = models.CharField(max_length=50, choices=yes_or_no_options, null=True)
    drinker = models.CharField(max_length=50, choices=yes_or_no_options, null=True)
    occupation = models.CharField(max_length=50, null=True)
    bio = models.TextField(null=True)
    favorite_place_ever_been = models.TextField(null=True)

    @property
    def age(self):
        today = timezone.now().date()
        age = int(
            today.year
            - (self.birth_date.year)
            - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        )
        return age

    def __str__(self) -> str:
        return self.user_profile.first_name


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
        ("Long-term", "Long-term partner"),
        ("Short-term", "Short-term partner"),
        ("Firguring-out", "Still figuring out"),
    )
    music_options = (
        ("Metal", "METAL"),
        ("Classic", "CLASSIC"),
        ("Country", "COUNTRY"),
        ("Pop", "POP"),
        ("Hip-hop", "HIP-HOP"),
        ("Gospel", "GOSPEL"),
    )
    outdoor_indoor_options = (("Outdoor", "OUTDOOR"), ("Indoor", "INDOOR"))
    what_do_you_do_for_fun_options = (
        ("Hiking", "HIKING"),
        ("Gaming", "GAMING"),
        ("Reading", "READING"),
        ("Singing", "SINGING"),
        ("Sports", "SPORTS"),
        ("Dancing", "DANCING"),
        ("Travel", "TRAVEL"),
        ("Poetry", "POETRY"),
        ("Music", "MUSIC"),
    )
    movie_genre_options = (
        ("Horror", "HORROR"),
        ("Romance", "ROMANCE"),
        ("Comedy", "COMEDY"),
        ("Action", "ACTION"),
        ("Anime", "ANIME"),
        ("Sci-fi", "SCI-FI"),
    )
    hobby_options = (
        ("Biking", "BIKING"),
        ("Knitting", "KNITTING"),
        ("Painting", "PAINTING"),
        ("Bird-watching", "BIRD-WATCHING"),
        ("Antiquing", "ANTIQUING"),
        ("Couch-Potato", "COUCH-POTATO"),
        ("Kayaking", "KAYAKING"),
        ("Swimming", "SWIMMING"),
    )
    sport_interest_options = (
        ("Baseball", "BASEBALL"),
        ("Basketball", "BASKETBALL"),
        ("Tennis", "TENNIS"),
        ("Football", "FOOTBALL"),
        ("Soccer", "SOCCER"),
        ("Skate", "SKATING"),
        ("Golf", "GOLF"),
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
    hobby_pick = models.CharField(max_length=300, choices=hobby_options, null=True)
    sport_pick = models.CharField(
        max_length=300, choices=sport_interest_options, null=True
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

    content = models.TextField(null=True)
    status = models.BooleanField(default=False, null=True)
    received_date = models.DateTimeField(auto_now_add=True, null=True)
    parent_message = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="replies"
    )


# class ProfileMessage(models.Model):
#     read = models.BooleanField(default=False)
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     message = models.ForeignKey(
#         Message, on_delete=models.CASCADE, related_name="profile_messages"
#     )
