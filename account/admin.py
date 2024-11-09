from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.utils.translation import gettext_lazy as _

# Define a custom UserAdmin
class CustomUserAdmin(UserAdmin):
    # Add the custom fields for is_student, is_parent, is_faculty, and is_coordinator
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Roles'), {'fields': ('is_student', 'is_parent', 'is_faculty', 'is_coordinator')}),
    )
    
    # Define the list display to show custom user fields in the admin user list
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_student', 'is_parent', 'is_faculty', 'is_coordinator', 'is_staff')
    
    # Add the custom fields to be filterable in the user list
    list_filter = ('is_student', 'is_parent', 'is_faculty', 'is_coordinator', 'is_staff', 'is_superuser', 'is_active', 'groups')

    # Define the fields that can be edited inline in the user list view
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

# Register the custom user admin
admin.site.register(User, CustomUserAdmin)
