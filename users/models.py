from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='roles')
    role_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.username} - {self.role_name}"

class UserPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='preferences')
    receive_newsletter = models.BooleanField(default=False)
    theme_color = models.CharField(max_length=20, default='light')

    def __str__(self):
        return f"{self.user.username}'s Preferences"