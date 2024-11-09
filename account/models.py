from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField('Is student', default=False)
    is_parent = models.BooleanField('Is parent', default=False)
    is_faculty = models.BooleanField('Is faculty', default=False)
    is_coordinator = models.BooleanField('Is course coordinator', default=False)
