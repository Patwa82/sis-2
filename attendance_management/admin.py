# attendance_management/admin.py

from django.contrib import admin
from .models import Attendance

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['student', 'date', 'status', 'program', 'branch']  # Add program and branch to list display
    search_fields = ['student__username', 'date']  # Updated search field to reference the user model
    list_filter = ['date', 'status', 'program', 'branch']  # Add program and branch to filters

admin.site.register(Attendance, AttendanceAdmin)
