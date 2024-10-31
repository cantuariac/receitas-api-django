from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('chef', 'Chef'),
        ('reader', 'Reader'),
    )

    role = models.CharField(max_length=15, choices=ROLE_CHOICES)
