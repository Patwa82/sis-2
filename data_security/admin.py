# data_security/admin.py

from django.contrib import admin
from .models import UserRole, DataEncryption, AuditLog

class UserRoleAdmin(admin.ModelAdmin):
    list_display = ['role_name']
    search_fields = ['role_name']

class DataEncryptionAdmin(admin.ModelAdmin):
    list_display = ['data_field', 'encryption_method', 'created_at']
    search_fields = ['data_field']

class AuditLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'action', 'ip_address', 'timestamp']
    search_fields = ['user__username', 'action', 'ip_address']

admin.site.register(UserRole, UserRoleAdmin)
admin.site.register(DataEncryption, DataEncryptionAdmin)
admin.site.register(AuditLog, AuditLogAdmin)
