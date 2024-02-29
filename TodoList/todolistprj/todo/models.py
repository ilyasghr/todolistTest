# models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import timedelta

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']

@receiver(post_save, sender=Task)
def send_notification(sender, instance, **kwargs):
    if instance.time:
        notification_time = instance.time - timedelta(hours=3)
        current_time = timezone.now()
        if notification_time <= current_time < instance.time:
            # Send notification logic goes here
            # You can use your preferred method for sending notifications
            # For example, you can use Django's built-in mail system or a third-party service
            # Example of sending an email:
            # user_email = instance.user.email
            # send_email(user_email, "Task Notification", "You have a task coming up in 3 hours.")
            print("Notification sent for task:", instance.title)
