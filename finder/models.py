from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# 1. Custom User model for User/Administrator roles
class CustomUser(AbstractUser):
    is_administrator = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username

# 2. Model for the Lost/Found items
class Item(models.Model):
    STATUS_CHOICES = [
        ('lost', 'Lost'),
        ('found', 'Found'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=5, choices=STATUS_CHOICES)
    date_reported = models.DateTimeField(auto_now_add=True)
    
    # Links the item to the user who reported it
    reported_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.get_status_display()})"