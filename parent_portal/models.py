from django.db import models
from django.conf import settings  # Use AUTH_USER_MODEL for relationships

# Model for Progress Report
class ProgressReport(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='progress_reports')  # Reference the user model for students
    faculty = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='faculty_reports')  # Faculty who creates the report
    subject = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    comments = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.student.username} - {self.subject} - {self.grade}"

# Model for Behavior
class Behavior(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='behaviors')  # Reference the user model for students
    behavior_type = models.CharField(max_length=50, choices=[('Positive', 'Positive'), ('Negative', 'Negative')])
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.student.username} - {self.behavior_type} - {self.date}"

# Model for Event Notification
class EventNotification(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='event_notifications')  # Reference the user model for students
    event_description = models.TextField()
    event_date = models.DateField()

    def __str__(self):
        return f"{self.student.username} - {self.event_date}"
