# assignment_management/forms.py

from django import forms
from .models import StudentAssignment, FacultyAssignment

class StudentAssignmentForm(forms.ModelForm):
    class Meta:
        model = StudentAssignment
        fields = ['program', 'title', 'description', 'student', 'due_date', 'submission_file', 'subject']  # Remove 'assignment'

class FacultyAssignmentForm(forms.ModelForm):
    class Meta:
        model = FacultyAssignment
        fields = ['student_assignment', 'feedback', 'auto_grade', 'assignment_file', 'program', 'subject']  # Ensure the fields match your model
