from django import forms
from .models import UserRole

class UserRoleForm(forms.ModelForm):
    class Meta:
        model = UserRole
        fields = ['role_name', 'permissions']
        widgets = {
            'permissions': forms.Textarea(attrs={'placeholder': 'Enter permissions in JSON format', 'class': 'form-control'}),
        }
        labels = {
            'role_name': 'Role Name',
            'permissions': 'Permissions',
        }
