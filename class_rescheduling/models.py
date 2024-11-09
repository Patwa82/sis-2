from django.db import models
from django.conf import settings  # Import settings for AUTH_USER_MODEL
from course_management.models import CollegeProgram, Branch, Subject

# Model for Class Schedule
class ClassSchedule(models.Model):
    class_name = models.CharField(max_length=100)
    instructor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Updated to use AUTH_USER_MODEL
    day_of_week = models.CharField(max_length=10)  # e.g., Monday
    start_time = models.TimeField()
    end_time = models.TimeField()
    program = models.ForeignKey(CollegeProgram, on_delete=models.CASCADE, null=True, blank=True)  # Allow null temporarily
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default=None)  # Corrected ForeignKey to Subject
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)  # Allow null temporarily

    def __str__(self):
        return f"{self.class_name} - {self.instructor} on {self.day_of_week} ({self.program.name if self.program else 'No Program'})"  # Updated the string

# Model for Time Table Notification
class TimeTableNotification(models.Model):
    schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE)
    message = models.TextField()
    notification_time = models.DateTimeField()

    def __str__(self):
        return f"Notification for {self.schedule.class_name} at {self.notification_time}"
