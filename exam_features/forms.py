# exam_features/forms.py

from django import forms
from .models import Exam, StudentSubmission, Grade

class ExamUploadForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['program', 'branch', 'year', 'subject', 'exam_file', 'start_time', 'end_time']  # Replace 'course' with 'program'
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class StudentSubmissionForm(forms.ModelForm):
    class Meta:
        model = StudentSubmission
        fields = ['program', 'branch', 'year', 'subject', 'submission_file']  # Replace 'course' with 'program'

class GradeUploadForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['exam', 'student', 'grade', 'marks']
