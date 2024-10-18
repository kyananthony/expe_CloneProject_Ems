from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import users
from .forms import EmployeeRegisterForm, EmployeeLoginForm
from .models import AuthCode, Attendance
from django.utils import timezone
from .models import TimeLog
from django.contrib.auth import views as auth_views

def register(request):
    if request.method == 'POST':
        form = EmployeeRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = EmployeeRegisterForm()
    return render(request, 'attendance/register.html', {'form': form})

def employee_login(request):
    if request.method == 'POST':
        form = EmployeeLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            auth_code = form.cleaned_data.get('auth_code')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                code_obj = AuthCode.objects.filter(user=user, code=auth_code, is_active=True).first()
                if code_obj:
                    login(request, user)
                    return redirect('time_in')
                else:
                    # Invalid auth code
                    form.add_error('auth_code', 'Invalid authentication code')
    else:
        form = EmployeeLoginForm()
    return render(request, 'attendance/login.html', {'form': form})


def time_in(request):
    if request.method == "POST":
        # Create a new TimeLog entry for the user
        TimeLog.objects.create(user=request.user, time_in=timezone.now())
        return redirect('time_log')  # Redirect to the time log page

    return render(request, 'attendance/time_in.html')

def time_out(request):
    if request.method == "POST":
        # Get the latest time log entry for the user
        time_log = TimeLog.objects.filter(user=request.user, time_out=None).last()
        if time_log:
            time_log.time_out = timezone.now()
            time_log.save()
        return redirect('time_log')  # Redirect to the time log page

    return render(request, 'attendance/time_out.html')

def time_log(request):
    # Get all time logs for the user
    time_logs = TimeLog.objects.filter(user=request.user).order_by('-time_in')
    return render(request, 'attendance/time_log.html', {'time_logs': time_logs})
def auth_code_view(request):
    if request.method == 'POST':
        auth_code = request.POST['auth_code']
        user_id = request.session.get('user_id')
        user = users.objects.get(id=user_id)

        # Check if the auth code matches
        if user.profile.auth_code == auth_code:
            login(request, user)  # Log in the user after successful validation
            return redirect('home')  # Redirect to home page or dashboard
        else:
            return render(request, 'auth_code.html', {'error': 'Invalid auth code'})

    return render(request, 'auth_code.html')
def dashboard(request):
    employee = Employee.objects.get(user=request.user)
    leave_balance = LeaveBalance.objects.get(employee=employee)
    attendance_records = Attendance.objects.filter(employee=employee).order_by('date')[:30]
    context = {
        'employee': employee,
        'leave_balance': leave_balance,
        'attendance_records': attendance_records,
    }
    return render(request, 'ems/dashboard.html', context)
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
