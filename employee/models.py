from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone


class Employee(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Manager', 'Manager'),
        ('Staff', 'Staff'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Leave(models.Model):
    LEAVE_TYPE_CHOICES = [
        ('PTO', 'Paid Time Off'),
        ('SICK', 'Sick Leave'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='leaves', null= True)
    leave_type = models.CharField(max_length=10, choices=LEAVE_TYPE_CHOICES)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.leave_type} Leave for {self.employee} from {self.start_date} to {self.end_date}"


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField()
    is_present = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.employee} - {self.date} - {'Present' if self.is_present else 'Absent'}"
