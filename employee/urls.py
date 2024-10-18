from django.urls import path,include
from . import views
from .views import LoginView, LogoutView
from .views import admin as adminView

urlpatterns = [
    path('/', views.employee_list, name='employee_list'),
    path('<int:pk>/', views.employee_detail, name='employee_detail'),
    path('create/', views.employee_create, name='employee_create'),
    path('<int:pk>/edit/', views.employee_update, name='employee_update'),
    path('<int:pk>/delete/', views.employee_delete, name='employee_delete'),
    path('admin/', admin.site.urls),
    path('employee/', include('employee.urls')),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
