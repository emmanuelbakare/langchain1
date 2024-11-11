from django.contrib import admin
from .models import Employee, Department, Feedback, ConflictResolution

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'hire_date', 'position', 'department')
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'manager')
    search_fields = ('name',)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('employee', 'feedback_date', 'comments', 'created_by')
    search_fields = ('employee__first_name', 'employee__last_name', 'comments')

@admin.register(ConflictResolution)
class ConflictResolutionAdmin(admin.ModelAdmin):
    list_display = ('employee', 'resolution_date', 'description', 'resolved_by')
    search_fields = ('employee__first_name', 'employee__last_name', 'description')