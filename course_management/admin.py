# course_management/admin.py
from django.contrib import admin
from django import forms
from .models import CollegeProgram, Branch, Subject

class CollegeProgramAdminForm(forms.ModelForm):
    dates = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter dates in YYYY-MM-DD format, separated by commas'}))

    class Meta:
        model = CollegeProgram
        fields = '__all__'

class CollegeProgramAdmin(admin.ModelAdmin):
    form = CollegeProgramAdminForm
    list_display = ['program', 'description', 'dates', 'enrollment_term']
    search_fields = ['program', 'description']
    list_filter = ['enrollment_term']

class BranchAdmin(admin.ModelAdmin):
    list_display = ['name', 'program']
    search_fields = ['name']

admin.site.register(CollegeProgram, CollegeProgramAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Subject)
