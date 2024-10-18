from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Employee, LeaveRequest, Attendance, LeaveBalance

def dashboard(request):
    employee = Employee.objects.get(user=request.user)
    leave_balance = LeaveBalance.objects.get(employee=employee)
    attendance_records = Attendance.objects.filter(employee=employee).order_by('date')[:30]
    context = {
        'employee': employee,
        'leave_balance': leave_balance,
        'attendance_records': attendance_records,
    }
    return render(request, 'ems/dashboard.html', {'employee':employee})
def request_leave(request, Leave=None):
    if request.method == 'POST':
        leave_type = request.POST['leave_type']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        reason = request.POST['reason']

        employee = Employee.objects.get(user=request.user)
        leave_request = Leave.Request.objects.create(
            employee=employee,
            leave_type=leave_type,
            start_date=start_date,
            end_date=end_date,
            reason=reason,
        )
        return render(request,'ems/request_leave.html')
# Create your views here.
def register(request):
    return None