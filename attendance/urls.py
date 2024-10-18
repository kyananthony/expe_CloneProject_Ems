from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import auth_code_view

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.employee_login, name='login'),
    path('time_in/', views.time_in, name='time_in'),
    path('time_out/', views.time_out, name='time_out'),
    path('time_log/', views.time_log, name='time_log'),
    path('auth_code/',auth_code_view,name='auth_code'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/uidb64/token/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('request-leave/',views.request_leave,name='request_leave'),
]
