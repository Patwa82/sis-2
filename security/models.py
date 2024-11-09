from django.db import models
from django.conf import settings  # Use AUTH_USER_MODEL for user references

class UserRole(models.Model):
    role_name = models.CharField(max_length=100)
    permissions = models.TextField()  # Store permissions as a JSON string or text

    def __str__(self):
        return self.role_name

class Encryption(models.Model):
    data_field = models.CharField(max_length=200)
    encrypted_value = models.TextField()
    encryption_method = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.data_field

class AuditLog(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='security_audit_logs'  # Add a unique related_name
    )
    action = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Audit log: {self.user.username} - {self.action} on {self.timestamp}"
