# assignment_management/models.py

from django.conf import settings  # Use settings for AUTH_USER_MODEL
from django.db import models
from course_management.models import CollegeProgram, Subject, Branch  # Import Subject from course_management

class StudentAssignment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Updated to use AUTH_USER_MODEL
    due_date = models.DateField()
    submitted = models.BooleanField(default=False)
    submission_date = models.DateField(null=True, blank=True)
    submission_file = models.FileField(upload_to='student_assignments/', null=True, blank=True)  # For file upload
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default=1)  # Default to a valid Subject ID
    program = models.ForeignKey(CollegeProgram, on_delete=models.CASCADE, null=True, blank=True)  # Allow null temporarily


    def is_late(self):
        """Check if the assignment is submitted late."""
        if self.submitted and self.submission_date > self.due_date:
            return True
        return False

    def __str__(self):
        return self.title


class FacultyAssignment(models.Model):
    student_assignment = models.ForeignKey(StudentAssignment, on_delete=models.CASCADE)
    feedback = models.TextField(null=True, blank=True)
    auto_grade = models.FloatField(null=True, blank=True)  # Store the auto grade
    assignment_file = models.FileField(upload_to='faculty_assignments/', null=True, blank=True)  # File upload for assignments
    program = models.ForeignKey(CollegeProgram, on_delete=models.CASCADE, null=True, blank=True)  # Allow null temporarily
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default=1)  # Default to a valid Subject ID
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)  # Allow null temporarily

    def __str__(self):
        return f"Feedback for {self.student_assignment.title}"

    def auto_grade_assignment(self):
        """Auto-grade based on certain criteria."""
        if self.student_assignment.submitted:
            self.auto_grade = 100  # Example: Give full marks for now
            self.save()



















    