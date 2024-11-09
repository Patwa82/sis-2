from django import forms
from .models import SupportRequest

class SupportRequestForm(forms.ModelForm):
    class Meta:
        model = SupportRequest
        fields = ['email', 'request_type', 'description']  # Removed 'student'

    # Customize the form fields
    request_type = forms.ChoiceField(choices=SupportRequest.SUPPORT_TYPES, label="Support Type")
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Describe your issue or request...'}))
