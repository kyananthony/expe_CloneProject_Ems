from django.db import models
from django.contrib.auth.models import User

from employee.models import Employee


class EMS(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'ems_profile')
    total_vacation_days = models.IntegerField(default=20)  # Total vacation days per year
    used_vacation_days = models.IntegerField(default=0)     # Vacation days used

    @property
    def remaining_vacation_days(self):
        return self.total_vacation_days - self.used_vacation_days

    def __str__(self):
        return self.user.username

class LeaveRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    leave_type = models.CharField(max_length=50)  # e.g., 'Vacation', 'Sick Leave'
    status = models.CharField(max_length=20, default='Pending')  # e.g., 'Approved', 'Rejected'

    def __str__(self):
        return f"{self.leave_type} request by {self.employee.user.username}"