from django.views.generic import ListView, CreateView
from .models import UserRole, AuditLog
from django.urls import reverse_lazy
from .forms import UserRoleForm

class UserRoleListView(ListView):
    model = UserRole
    template_name = 'security/user_role_management.html'
    context_object_name = 'roles'

class UserRoleCreateView(CreateView):
    model = UserRole
    form_class = UserRoleForm  # Use the form we created for user roles
    template_name = 'security/user_role_create.html'
    success_url = reverse_lazy('user_role_list')

class AuditLogListView(ListView):
    model = AuditLog
    template_name = 'security/audit_logs.html'
    context_object_name = 'logs'
    paginate_by = 10  # Add pagination for audit logs
