from django.urls import path
from .views import UserRoleListView, UserRoleCreateView, AuditLogListView

urlpatterns = [
    path('roles/', UserRoleListView.as_view(), name='user_role_list'),
    path('roles/create/', UserRoleCreateView.as_view(), name='user_role_create'),
    path('logs/', AuditLogListView.as_view(), name='audit_log_list'),
]
