# exam_features/admin.py

from django.contrib import admin
from .models import Exam, StudentSubmission, Grade

class ExamAdmin(admin.ModelAdmin):
    list_display = ['program', 'branch', 'year', 'subject', 'uploaded_by', 'start_time', 'end_time']
    search_fields = ['program__name', 'branch__name', 'subject', 'year']
    list_filter = ['program', 'branch', 'year', 'start_time', 'end_time']

class StudentSubmissionAdmin(admin.ModelAdmin):
    list_display = ['student', 'exam', 'submitted_on', 'submission_file']
    search_fields = ['student__username', 'exam__subject', 'exam__program__name', 'branch__name', 'year']
    list_filter = ['submitted_on', 'exam__program', 'branch', 'year']

class GradeAdmin(admin.ModelAdmin):
    list_display = ['exam', 'student', 'grade', 'marks']
    search_fields = ['exam__program__name', 'exam__subject', 'student__username']
    list_filter = ['exam__program', 'exam__branch', 'exam__year']

admin.site.register(Exam, ExamAdmin)
admin.site.register(StudentSubmission, StudentSubmissionAdmin)
admin.site.register(Grade, GradeAdmin)
