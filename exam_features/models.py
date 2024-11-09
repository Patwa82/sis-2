# exam_features/models.py

from django.db import models
from django.conf import settings
from course_management.models import CollegeProgram, Branch
from django.utils import timezone

class Exam(models.Model):
    program = models.ForeignKey(CollegeProgram, on_delete=models.CASCADE, null=True, blank=True)  # Allow null temporarily
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)  # Allow null temporarily
    year = models.PositiveIntegerField()
    subject = models.CharField(max_length=100)
    exam_file = models.FileField(upload_to='faculty_exams/', null=True, blank=True)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='uploaded_exams')  # Keep this field once
    upload_date = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def is_exam_active(self):
        now = timezone.now()
        return self.start_time <= now <= self.end_time

    def __str__(self):
        return f"{self.program.name} - {self.subject} ({self.branch.name}, Year {self.year})"

class StudentSubmission(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='exam_submissions')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    submission_file = models.FileField(upload_to='student_submissions/', null=True, blank=True)
    submitted_on = models.DateTimeField(auto_now_add=True)
    program = models.ForeignKey(CollegeProgram, on_delete=models.CASCADE, null=True, blank=True)  # Allow null temporarily
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)  # Allow null temporarily
    year = models.PositiveIntegerField()
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.student.username} - {self.exam.subject} ({self.branch.name}, Year {self.year})"

class Grade(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='grades')
    marks = models.FloatField()
    grade = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.student.username} - {self.exam.subject} - {self.grade}"
