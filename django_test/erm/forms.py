from django import forms
from .models import Employee, Department, Feedback, ConflictResolution


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'hire_date', 'position', 'department']


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'manager']


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['employee', 'feedback_date', 'comments', 'created_by']


class ConflictResolutionForm(forms.ModelForm):
    class Meta:
        model = ConflictResolution
        fields = ['employee', 'resolution_date', 'description', 'resolved_by']
