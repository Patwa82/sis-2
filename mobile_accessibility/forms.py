# mobile_accessibility/forms.py

from django import forms
from .models import MobileNotification

# Form for creating or updating mobile notifications
class MobileNotificationForm(forms.ModelForm):
    class Meta:
        model = MobileNotification
        fields = ['title', 'message']  # Fields to be displayed in the form

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter notification title', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'Enter notification message', 'class': 'form-control'}),
        }

        labels = {
            'title': 'Notification Title',
            'message': 'Notification Message',
        }
