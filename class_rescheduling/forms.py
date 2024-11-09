from django import forms
from .models import ClassSchedule, TimeTableNotification
from course_management.models import CollegeProgram, Subject  # Updated import

class ClassScheduleForm(forms.ModelForm):
    class Meta:
        model = ClassSchedule
        fields = ['class_name', 'instructor', 'day_of_week', 'start_time', 'end_time', 'program', 'subject']  # Replace 'course' with 'program'

    program = forms.ModelChoiceField(queryset=CollegeProgram.objects.all(), label="Program")  # Updated to 'program'
    subject = forms.ModelChoiceField(queryset=Subject.objects.all(), label="Subject")

class TimeTableNotificationForm(forms.ModelForm):
    class Meta:
        model = TimeTableNotification
        fields = ['schedule', 'message', 'notification_time']
