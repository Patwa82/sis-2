# attendance_management/models.py

from django.conf import settings  # Use settings for AUTH_USER_MODEL
from django.db import models
from django.utils import timezone
from course_management.models import CollegeProgram, Subject, Branch  # Import the updated models

class Attendance(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Updated to use AUTH_USER_MODEL
    date = models.DateField(default=timezone.now)  # Default to the current date
    status = models.BooleanField(default=False)  # True for present, False for absent
    program = models.ForeignKey(CollegeProgram, on_delete=models.CASCADE, null=True, blank=True)  # Allow null temporarily
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default=1)  # Default to a valid Subject ID
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)  # Allow null temporarily

    def __str__(self):
        return f"{self.student.username} - {self.date} - {self.program.name} - {self.subject.name}"

    @classmethod
    def mark_attendance(cls, student, status, program, subject):
        """Mark attendance for a student."""
        from datetime import date
        attendance, created = cls.objects.get_or_create(
            student=student, date=date.today(), program=program, subject=subject
        )
        attendance.status = status
        attendance.save()
