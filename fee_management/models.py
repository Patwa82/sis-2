from django.db import models
from course_management.models import CollegeProgram, Branch # Use CollegeProgram instead of Course
from django.conf import settings  # Import AUTH_USER_MODEL

# Model for Fee Payment
class FeePayment(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Link to custom User model
    program = models.ForeignKey(CollegeProgram, on_delete=models.CASCADE, null=True, blank=True)  # Allow null temporarily
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)  # Allow null temporarily
    year = models.PositiveIntegerField(default=None)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    receipt_number = models.CharField(max_length=100, unique=True)
    is_online = models.BooleanField(default=False)  # Field for Online Payment Status

    def __str__(self):
        return f"{self.student.username} - {self.amount} on {self.payment_date}"

# Model for Penalty
class Penalty(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Link to custom User model
    program = models.ForeignKey(CollegeProgram, on_delete=models.CASCADE, null=True, blank=True)  # Allow null temporarily
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)  # Allow null temporarily
    penalty_amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.TextField()
    penalty_date = models.DateField()

    def __str__(self):
        return f"Penalty for {self.student.username} - {self.penalty_amount}"
