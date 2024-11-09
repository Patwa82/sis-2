# mobile_accessibility/admin.py

from django.contrib import admin
from .models import MobileNotification

class MobileNotificationAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_sent', 'sent_by']  # Show sent_by in the admin panel
    search_fields = ['title', 'sent_by__username']  # Allow search by user who sent the notification
    list_filter = ['date_sent', 'sent_by']

admin.site.register(MobileNotification, MobileNotificationAdmin)
