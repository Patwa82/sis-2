# communication_tools/models.py

from django.db import models
from django.conf import settings
from course_management.models import CollegeProgram, Branch  # Import CollegeProgram and Branch

class DiscussionForum(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    program = models.ForeignKey(CollegeProgram, on_delete=models.CASCADE, null=True, blank=True)  # Allow null temporarily
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)  # Allow null temporarily

    def __str__(self):
        return self.title

class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Use AUTH_USER_MODEL
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username} - {self.message}"

class AdminNotification(models.Model):
    admin_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='admin_notifications')  # Use AUTH_USER_MODEL
    action = models.CharField(max_length=200)
    details = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Admin Notification for {self.admin_user.username}: {self.action}"
