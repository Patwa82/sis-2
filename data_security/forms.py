# data_security/forms.py

from django import forms
from .models import UserRole, DataEncryption

# UserRole form
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

# DataEncryption form
class DataEncryptionForm(forms.ModelForm):
    class Meta:
        model = DataEncryption
        fields = ['data_field', 'encrypted_value', 'encryption_method']
        widgets = {
            'data_field': forms.TextInput(attrs={'class': 'form-control'}),
            'encrypted_value': forms.Textarea(attrs={'class': 'form-control'}),
            'encryption_method': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'data_field': 'Data Field',
            'encrypted_value': 'Encrypted Value',
            'encryption_method': 'Encryption Method',
        }
