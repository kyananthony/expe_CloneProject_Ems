from django.urls import path
from .import views

urlpatterns = [
    path('dashboard/',views.dashboard,name='dashboard'),
    path('request-leave/',views.request_leave,name='request_leave'),
]