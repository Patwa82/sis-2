# communication_tools/forms.py

from django import forms
from .models import DiscussionForum
from course_management.models import CollegeProgram, Branch  # Replace Course with CollegeProgram

class DiscussionForumForm(forms.ModelForm):
    class Meta:
        model = DiscussionForum
        fields = ['title', 'content', 'program', 'branch']  # Update to 'program' and 'branch'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['program'].queryset = CollegeProgram.objects.all()  # Query CollegeProgram
        self.fields['branch'].queryset = Branch.objects.all()  # Query Branch
