# performance_analytics/admin.py

from django.contrib import admin
from .models import StudentPerformance

class StudentPerformanceAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'score', 'date', 'behavior', 'program', 'grade']  # Replace 'course' with 'program'
    search_fields = ['student__username', 'subject', 'program__name', 'grade__grade']  # Allow searching by student, program, grade
    list_filter = ['subject', 'date', 'program', 'grade']  # Filters for quick access

admin.site.register(StudentPerformance, StudentPerformanceAdmin)
