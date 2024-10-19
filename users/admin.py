from django.contrib import admin
from .models import UserProfile, UserRole, UserPreferences

admin.site.register(UserProfile)
admin.site.register(UserRole)
admin.site.register(UserPreferences)
# Register your models here.
