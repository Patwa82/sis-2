# data_security/views.py

from django.views.generic import ListView, CreateView
from .models import UserRole, DataEncryption, AuditLog
from .forms import UserRoleForm, DataEncryptionForm
from django.urls import reverse_lazy

# User Role Management Views
class UserRoleListView(ListView):
    model = UserRole
    template_name = 'data_security/user_roles.html'
    context_object_name = 'roles'

class UserRoleCreateView(CreateView):
    model = UserRole
    form_class = UserRoleForm
    template_name = 'data_security/user_role_create.html'
    success_url = reverse_lazy('user_role_list')

# Data Encryption Views
class DataEncryptionListView(ListView):
    model = DataEncryption
    template_name = 'data_security/encryption_list.html'
    context_object_name = 'encryptions'

class DataEncryptionCreateView(CreateView):
    model = DataEncryption
    form_class = DataEncryptionForm
    template_name = 'data_security/encryption_create.html'
    success_url = reverse_lazy('encryption_list')

# Audit Log Views
class AuditLogListView(ListView):
    model = AuditLog
    template_name = 'data_security/audit_log.html'
    context_object_name = 'logs'
    paginate_by = 10  # Paginate logs
