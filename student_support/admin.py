from django.contrib import admin
from .models import SupportRequest

class SupportRequestAdmin(admin.ModelAdmin):
    list_display = ['student', 'request_type', 'submitted_at']  # Use student instead of student_name
    search_fields = ['student__username', 'request_type']
    list_filter = ['request_type', 'submitted_at']

admin.site.register(SupportRequest, SupportRequestAdmin)
