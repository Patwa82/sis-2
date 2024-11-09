from django.contrib import admin
from .models import ProgressReport, Behavior, EventNotification

class ProgressReportAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'grade', 'date']
    search_fields = ['student__username', 'subject']  # Updated to use student username
    list_filter = ['date']

class BehaviorAdmin(admin.ModelAdmin):
    list_display = ['student', 'behavior_type', 'date']
    search_fields = ['student__username', 'behavior_type']  # Updated to use student username
    list_filter = ['date']

class EventNotificationAdmin(admin.ModelAdmin):
    list_display = ['student', 'event_date']
    search_fields = ['student__username']  # Updated to use student username
    list_filter = ['event_date']

admin.site.register(ProgressReport, ProgressReportAdmin)
admin.site.register(Behavior, BehaviorAdmin)
admin.site.register(EventNotification, EventNotificationAdmin)
