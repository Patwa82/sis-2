from django.contrib import admin
from .models import StudentAssignment, FacultyAssignment

@admin.register(StudentAssignment)
class StudentAssignmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'due_date', 'student', 'submitted']
    search_fields = ['title', 'student']

@admin.register(FacultyAssignment)
class FacultyAssignmentAdmin(admin.ModelAdmin):
    list_display = ['student_assignment', 'auto_grade']
    search_fields = ['student_assignment__title']
