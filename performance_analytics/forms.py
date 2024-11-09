# performance_analytics/forms.py

from django import forms
from .models import StudentPerformance
from exam_features.models import Exam, Grade  # Import Exam and Grade models
from course_management.models import CollegeProgram  # Replace Course with CollegeProgram
from django.contrib.auth import get_user_model  # Use custom user model

User = get_user_model()

class StudentPerformanceForm(forms.ModelForm):
    class Meta:
        model = StudentPerformance
        fields = ['student', 'exam', 'program', 'branch', 'subject', 'score', 'date', 'behavior', 'grade']  # Replace 'course' with 'program'

    # Customizing fields
    student = forms.ModelChoiceField(queryset=User.objects.all(), label="Student")
    exam = forms.ModelChoiceField(queryset=Exam.objects.all(), label="Exam", required=False)
    program = forms.ModelChoiceField(queryset=CollegeProgram.objects.all(), label="Program")  # Updated to CollegeProgram
    subject = forms.CharField(max_length=100, label="Subject")
    score = forms.FloatField(label="Score")
    date = forms.DateField(widget=forms.SelectDateWidget, label="Date")
    behavior = forms.ChoiceField(choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Average', 'Average'), ('Poor', 'Poor')], label="Behavior")
    grade = forms.ModelChoiceField(queryset=Grade.objects.all(), label="Grade", required=False)
