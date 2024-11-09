# performance_analytics/models.py

from django.db import models
from django.conf import settings  # Use AUTH_USER_MODEL for student reference
from exam_features.models import Exam, Grade  # Import Exam and Grade models
from course_management.models import CollegeProgram, Branch  # Use CollegeProgram instead of Course

class StudentPerformance(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='performances')  # Reference the user model for students
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, null=True, blank=True)  # Link to exam, optional
    program = models.ForeignKey(CollegeProgram, on_delete=models.CASCADE, null=True, blank=True)  # Allow null temporarily
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)  # Allow null temporarily
    grade = models.ForeignKey(Grade, on_delete=models.SET_NULL, null=True, blank=True)  # Link to Grade model
    score = models.FloatField()  # Exam score
    subject = models.CharField(max_length=100)  # Subject related to the performance
    date = models.DateField()  # Date of the performance
    behavior = models.CharField(max_length=100, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Average', 'Average'), ('Poor', 'Poor')], default='Average')

    def __str__(self):
        return f"{self.student.username} - {self.subject} - {self.score} - {self.behavior} - {self.program.name}"  # Adjusted to program
