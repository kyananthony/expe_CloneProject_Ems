from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_in = models.DateTimeField(null=True, blank=True)
    time_out = models.DateTimeField(null=True, blank=True)
    date = models.DateField(default=timezone.now)


class AuthCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    is_active = models.BooleanField(default=True)  # Add is_active field
    created_at = models.DateTimeField(auto_now_add=True)  # Add created_at field

    def __str__(self):
        return f'{self.user.username} - {self.code}'

class TimeLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_in = models.DateTimeField(null=True, blank=True)
    time_out = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} - Time In: {self.time_in}, Time Out: {self.time_out}'

    def hours_worked(self):
        if self.time_in and self.time_out:
            return (self.time_out - self.time_in).total_seconds() / 3600  # Returns hours
        return 0
