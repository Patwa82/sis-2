# mobile_accessibility/models.py

from django.db import models
from django.conf import settings  # Import for AUTH_USER_MODEL

# Model for Mobile Notifications
class MobileNotification(models.Model):
    title = models.CharField(max_length=200)  # Title of the notification
    message = models.TextField()  # Message content of the notification
    date_sent = models.DateTimeField(auto_now_add=True)  # Automatically add the date when the notification is created
    sent_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Track which user sent the notification

    def __str__(self):
        return self.title
