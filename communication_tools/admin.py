# communication_tools/admin.py

from django.contrib import admin
from .models import DiscussionForum, Notification, AdminNotification

class DiscussionForumAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']

class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'message', 'is_read', 'created_at']
    search_fields = ['user__username', 'message']

class AdminNotificationAdmin(admin.ModelAdmin):
    list_display = ['admin_user', 'action', 'is_read', 'created_at']
    search_fields = ['admin_user__username', 'action']

admin.site.register(DiscussionForum, DiscussionForumAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(AdminNotification, AdminNotificationAdmin)
