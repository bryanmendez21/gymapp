from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users
# Register your models here.

#--REGISTER MODEL--
class CustomUserAdmin(UserAdmin):
    model = Users
    list_display = ['username', 'email', 'full_name', 'date_of_birth']

admin.site.register(Users, CustomUserAdmin)