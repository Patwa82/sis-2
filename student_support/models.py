from django.conf import settings  # Import the user model
from django.db import models

class SupportRequest(models.Model):
    SUPPORT_TYPES = [
        ('counseling', 'Counseling Support'),
        ('helpdesk', 'Student Helpdesk'),
    ]
    
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Link to user model
    email = models.EmailField()
    request_type = models.CharField(max_length=50, choices=SUPPORT_TYPES)
    description = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.get_request_type_display()}"
