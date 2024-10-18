from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE),
    position = models.CharField(max_length=100)
    hire_date = models.DateField()
class Attendance(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    is_present = models.BooleanField(default=True)
    check_in_time = models.TimeField(null=True, blank=True)
    check_out_time = models.TimeField(null=True, blank=True)
class LeaveRequest(models.Model):
    LEAVE_TYPES = [
        ('PTO','Paid Time Off'),
        ('SICK','Sick Leave')
    ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=4, choices=LEAVE_TYPES)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    approved = models.BooleanField(default=False)
    date_requested = models.DateField(auto_now_add=True)
class LeaveBalance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    pto_balance = models.FloatField(default=15)
    sick_leave_balance = models.FloatField(default=10)
# Create your models here.
