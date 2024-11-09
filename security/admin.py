from django.contrib import admin
from .models import UserRole, Encryption, AuditLog

class UserRoleAdmin(admin.ModelAdmin):
    list_display = ['role_name']
    search_fields = ['role_name']

class EncryptionAdmin(admin.ModelAdmin):
    list_display = ['data_field', 'encryption_method', 'created_at']
    search_fields = ['data_field']

class AuditLogAdmin(admin.ModelAdmin):
    list_display = ['action', 'user', 'timestamp']  # Display action, user, and timestamp
    search_fields = ['action', 'user__username']  # Enable search by action and user
    list_filter = ['timestamp']

admin.site.register(UserRole, UserRoleAdmin)
admin.site.register(Encryption, EncryptionAdmin)
admin.site.register(AuditLog, AuditLogAdmin)
