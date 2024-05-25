from django.db import models

# Create your models here.


class Profile(models.Model):
    fname = models.CharField()
    lname = models.CharField()
    profile_pic = models.CharField()


class Message(models.Model):
    sender = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, related_name="sender_notification"
    )
    recipient = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="recipient_notification"
    )
    content = models.TextField()
    read = models.BooleanField(default=False)
    recieved_date = models.DateTimeField(auto_now_add=True)
    profile = models.ManyToManyField(
        Profile, related_name="message", through="ProfileMessage"
    )


class ProfileMessage(models.Model):
    read = models.BooleanField()
    user = models.ForeignKey()
    message = models.ForeignKey(Message, related_name="profile_message")
