from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    profile_pic = models.ImageField(null=True)

class DatingProfile(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="dating_profile_user", null=True)
    gender_options = (('male', "MALE"), ('female', "FEMALE"))
    orientation_options = ("")
    yes_or_no_options = (("yes", "YES"), ('no', "NO"))
    gender = models.CharField(max_length=50, choices=gender_options)
    # orientation = models.CharField(max_length=50, choices=orientation_options)
    smoker = models.CharField(max_length=50, choices=yes_or_no_options)

class PersonalityProfile(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="personality_profile_user", null=True)

class Message(models.Model):
    sender = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, null=True, related_name="sent_messages"
    )
    recipient = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="received_messages",
        null=True
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
