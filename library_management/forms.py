# library_management/forms.py

from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['resource', 'return_date']
        widgets = {
            'return_date': forms.SelectDateWidget,
        }
        labels = {
            'resource': 'Select Resource',
            'return_date': 'Return Date',
        }

        # library_management/forms.py

from django import forms
from .models import Resource

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'author', 'published_date', 'is_available']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter author'}),
            'published_date': forms.SelectDateWidget(),
            'is_available': forms.CheckboxInput(),
        }
        labels = {
            'title': 'Resource Title',
            'author': 'Author Name',
            'published_date': 'Published Date',
            'is_available': 'Available',
        }

