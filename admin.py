from django.contrib import admin
from .models import Employee, Department, Feedback, Meeting

# Register the Department model
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location')  # Display these fields in the admin list view
    search_fields = ('name',)  # Allow searching by department name

# Register the Employee model
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'job_title', 'department')
    search_fields = ('first_name', 'last_name', 'email', 'job_title')
    list_filter = ('department',)  # Filter by department

# Register the Feedback model
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'date')
    search_fields = ('employee__first_name', 'employee__last_name')  # Allow searching by employee name

# Register the Meeting model
@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'location')
    search_fields = ('title', 'location')
    list_filter = ('date',)  # Filter by date
