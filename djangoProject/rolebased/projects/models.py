from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("worker", "Worker"),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="worker")

    def __str__(self):
        return f"{self.username} ({self.role})"


class Project(models.Model):
    STATUS_CHOICES = (
        ("InProgress", "In Progress"),
        ("Completed", "Completed"),
    )

    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="InProgress"
    )
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.status})"
