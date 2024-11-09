# course_management/models.py
from django.db import models

class CollegeProgram(models.Model):
    PROGRAM_CHOICES = [
        ('Business Program', 'Business Program'),
        ('Hospitality Program', 'Hospitality Program'),
        ('Digital Marketing', 'Digital Marketing'),
        ('Health Care Program', 'Health Care Program'),
        ('Community Programs', 'Community Programs'),
        ('Education Assist', 'Education Assist'),
    ]

    ENROLLMENT_TERM_CHOICES = [
        ('Spring', 'Spring'),
        ('Summer', 'Summer'),
        ('Fall', 'Fall'),
        ('Winter', 'Winter'),
    ]

    program = models.CharField(max_length=200, choices=PROGRAM_CHOICES, default='Business Program')
    description = models.TextField()
    dates = models.TextField(default=1)  # Store multiple dates as a comma-separated string
    enrollment_term = models.CharField(max_length=20, choices=ENROLLMENT_TERM_CHOICES, default='Spring')

    def __str__(self):
        return self.program


class Branch(models.Model):
    name = models.CharField(max_length=100)
    program = models.ForeignKey(CollegeProgram, related_name='branches', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch, related_name='subjects', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
