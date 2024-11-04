from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee, Department, Position, EmployeeRelation, Feedback, Meeting
from django.http import HttpResponse
from django.views import View

# Employee Views
class EmployeeListView(View):
    def get(self, request):
        employees = Employee.objects.all()
        return render(request, 'employee_list.html', {'employees': employees})

class EmployeeDetailView(View):
    def get(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        return render(request, 'employee_detail.html', {'employee': employee})

class EmployeeCreateView(View):
    def get(self, request):
        return render(request, 'employee_form.html')  # Add form handling

    def post(self, request):
        # Handle form submission
        return redirect('employee_list')

class EmployeeUpdateView(View):
    def get(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        return render(request, 'employee_form.html', {'employee': employee})  # Add form handling

    def post(self, request, pk):
        # Handle form update
        return redirect('employee_detail', pk=pk)


# Department Views
class DepartmentListView(View):
    def get(self, request):
        departments = Department.objects.all()
        return render(request, 'department_list.html', {'departments': departments})

class DepartmentDetailView(View):
    def get(self, request, pk):
        department = get_object_or_404(Department, pk=pk)
        return render(request, 'department_detail.html', {'department': department})


# Position Views
class PositionListView(View):
    def get(self, request):
        positions = Position.objects.all()
        return render(request, 'position_list.html', {'positions': positions})

class PositionDetailView(View):
    def get(self, request, pk):
        position = get_object_or_404(Position, pk=pk)
        return render(request, 'position_detail.html', {'position': position})


# EmployeeRelation Views
class EmployeeRelationListView(View):
    def get(self, request):
        relations = EmployeeRelation.objects.all()
        return render(request, 'employee_relation_list.html', {'relations': relations})


# Feedback Views
class FeedbackListView(View):
    def get(self, request):
        feedbacks = Feedback.objects.all()
        return render(request, 'feedback_list.html', {'feedbacks': feedbacks})


# Meeting Views
class MeetingListView(View):
    def get(self, request):
        meetings = Meeting.objects.all()
        return render(request, 'meeting_list.html', {'meetings': meetings})