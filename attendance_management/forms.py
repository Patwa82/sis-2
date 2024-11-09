# attendance_management/forms.py

from django import forms
from .models import Attendance
from course_management.models import CollegeProgram, Subject, Branch  # Import CollegeProgram and Subject models
from django.conf import settings  # Use settings for AUTH_USER_MODEL

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'status', 'program', 'subject', 'branch']  # Use 'program' instead of 'course'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['program'].queryset = CollegeProgram.objects.all()  # Adjust to query CollegeProgram instead of Course
        self.fields['subject'].queryset = Subject.objects.all()
        self.fields['branch'].queryset = Branch.objects.all()  # Query branches as per your updated model structure
        self.fields['student'].queryset = settings.AUTH_USER_MODEL.objects.filter(is_student=True)  # Optionally filter students
