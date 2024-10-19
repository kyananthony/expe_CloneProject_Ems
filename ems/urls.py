from django.urls import path
from .views import employee_view, request_leave

urlpatterns = [
    path('view/', employee_view, name='employee_view'),
    path('request-leave/', request_leave, name='request_leave'),
]