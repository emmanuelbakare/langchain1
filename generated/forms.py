from django import forms
from .models import Employee, Department, Feedback, Meeting

class EmployeeForm(forms.ModelForm):
    """
    Form for Employee model.
    """
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'hire_date', 'job_title', 'department', 'manager']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'hire_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'job_title': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'manager': forms.Select(attrs={'class': 'form-control'}),
        }

class DepartmentForm(forms.ModelForm):
    """
    Form for Department model.
    """
    class Meta:
        model = Department
        fields = ['name', 'location']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }

class FeedbackForm(forms.ModelForm):
    """
    Form for Feedback model.
    """
    class Meta:
        model = Feedback
        fields = ['employee', 'date', 'feedback_text']
        widgets = {
            'employee': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'feedback_text': forms.Textarea(attrs={'class': 'form-control'}),
        }

class MeetingForm(forms.ModelForm):
    """
    Form for Meeting model.
    """
    class Meta:
        model = Meeting
        fields = ['title', 'date', 'location', 'participants']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'participants': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }