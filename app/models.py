from django.db import models

# Create your models here.


class Profile(models.Model):
    fname = models.CharField()
    lname = models.CharField()
    profile_pic = models.CharField()


class Message(models.Model):
    sender = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, related_name="sent_messages"
    )
    recipient = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="received_messages",
        through="ProfileMessage",
    )
    # recipient = models.ManyToManyField(
    #     Profile,
    #     on_delete=models.CASCADE,
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
#     user = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     message = models.ForeignKey(
#         Message, on_delete=models.CASCADE, related_name="profile_messages"
#     )
