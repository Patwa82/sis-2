# course_management/forms.py
from django import forms
from .models import CollegeProgram, Branch

class CollegeProgramForm(forms.ModelForm):
    branches = forms.ModelMultipleChoiceField(queryset=Branch.objects.none(), widget=forms.CheckboxSelectMultiple)
    dates = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter dates in YYYY-MM-DD format, separated by commas'}))

    class Meta:
        model = CollegeProgram
        fields = ['program', 'description', 'enrollment_term', 'branches', 'dates']

    def __init__(self, *args, **kwargs):
        super(CollegeProgramForm, self).__init__(*args, **kwargs)
        if 'instance' in kwargs:
            self.fields['branches'].queryset = Branch.objects.filter(program=kwargs['instance'])

    def clean_dates(self):
        date_list = self.cleaned_data['dates'].split(',')
        cleaned_dates = []
        for date_str in date_list:
            date_str = date_str.strip()
            try:
                date_obj = forms.DateField().to_python(date_str)
                cleaned_dates.append(date_obj)
            except forms.ValidationError:
                raise forms.ValidationError(f"Invalid date format: {date_str}. Use YYYY-MM-DD format.")
        return cleaned_dates
