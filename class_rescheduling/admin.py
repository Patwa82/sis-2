from django.contrib import admin
from .models import ClassSchedule, TimeTableNotification

class ClassScheduleAdmin(admin.ModelAdmin):
    list_display = ['class_name', 'instructor', 'day_of_week', 'start_time', 'end_time', 'program', 'subject']  # Replace 'course' with 'program'
    search_fields = ['class_name', 'instructor__username', 'program__name', 'subject__name']  # Updated to 'program__name'
    list_filter = ['day_of_week', 'program']

class TimeTableNotificationAdmin(admin.ModelAdmin):
    list_display = ['schedule', 'message', 'notification_time']
    search_fields = ['schedule__class_name', 'message']
    list_filter = ['notification_time']

admin.site.register(ClassSchedule, ClassScheduleAdmin)
admin.site.register(TimeTableNotification, TimeTableNotificationAdmin)
