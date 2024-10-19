from django.shortcuts import render
from .models import Employee, LeaveRequest


def employee_view(request):
    employee = Employee.objects.get(user=request.user)
    leave_requests = LeaveRequest.objects.filter(employee=employee)

    context = {
        'employee': employee,
        'leave_requests': leave_requests,
    }
    return render(request, 'ems/employee_view.html', context)


def request_leave(request):
    if request.method == 'POST':
        # Handle leave request form submission
        # (Add form handling logic here)
        pass
    return render(request, 'ems/request_leave.html')