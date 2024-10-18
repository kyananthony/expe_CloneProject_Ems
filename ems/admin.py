from django.contrib import admin
from .models import Employee, Attendance, LeaveRequest, LeaveBalance

admin.site.register(Employee)
admin.site.register(Attendance)
admin.site.register(LeaveRequest)
admin.site.register(LeaveBalance)

# Register your models here.
