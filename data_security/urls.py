# data_security/urls.py

from django.urls import path
from .views import (
    UserRoleListView, UserRoleCreateView, 
    DataEncryptionListView, DataEncryptionCreateView, 
    AuditLogListView
)

urlpatterns = [
    # User Roles URLs
    path('roles/', UserRoleListView.as_view(), name='user_role_list'),
    path('roles/create/', UserRoleCreateView.as_view(), name='user_role_create'),

    # Data Encryption URLs
    path('encryption/', DataEncryptionListView.as_view(), name='encryption_list'),
    path('encryption/create/', DataEncryptionCreateView.as_view(), name='encryption_create'),

    # Audit Log URLs
    path('audit-log/', AuditLogListView.as_view(), name='audit_log'),
]
