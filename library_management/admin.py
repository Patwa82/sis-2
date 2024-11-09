

# library_management/admin.py

from django.contrib import admin
from .models import Resource, Booking

class ResourceAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_date', 'is_available']
    search_fields = ['title', 'author']

class BookingAdmin(admin.ModelAdmin):
    list_display = ['resource', 'booked_by', 'booking_date', 'return_date']
    search_fields = ['booked_by__username']  # Use 'booked_by__username' to search by username

admin.site.register(Resource, ResourceAdmin)
admin.site.register(Booking, BookingAdmin)
