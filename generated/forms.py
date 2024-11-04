from django import forms
from .models import Employee, Department, Position, EmployeeRelation, Feedback, Meeting

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'phone', 'hire_date', 'department', 'position']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']

class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['title']

class EmployeeRelationForm(forms.ModelForm):
    class Meta:
        model = EmployeeRelation
        fields = ['employee', 'relation_type', 'description']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['employee', 'feedback_text']

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['employee', 'meeting_date', 'agenda', 'notes']