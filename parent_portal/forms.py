from django import forms
from .models import ProgressReport, Behavior, EventNotification

class ProgressReportForm(forms.ModelForm):
    class Meta:
        model = ProgressReport
        fields = ['student', 'subject', 'grade', 'comments', 'date']  # Faculty selects the student for the report
        labels = {
            'student': 'Student',
            'subject': 'Subject',
            'grade': 'Grade',
            'comments': 'Comments',
            'date': 'Date',
        }

class BehaviorForm(forms.ModelForm):
    class Meta:
        model = Behavior
        fields = ['student', 'behavior_type', 'description', 'date']
        labels = {
            'student': 'Student',
            'behavior_type': 'Behavior Type',
            'description': 'Description',
            'date': 'Date',
        }

class EventNotificationForm(forms.ModelForm):
    class Meta:
        model = EventNotification
        fields = ['student', 'event_description', 'event_date']
        labels = {
            'student': 'Student',
            'event_description': 'Event Description',
            'event_date': 'Event Date',
        }
