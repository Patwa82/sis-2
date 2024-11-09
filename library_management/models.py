# library_management/models.py

from django.db import models
from django.conf import settings  # Use AUTH_USER_MODEL for user relationships

class Resource(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Booking(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    booked_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Link to custom User model
    booking_date = models.DateField(auto_now_add=True)
    return_date = models.DateField()

    def __str__(self):
        return f"{self.resource.title} booked by {self.booked_by.username}"
