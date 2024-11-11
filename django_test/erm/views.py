from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Department, Feedback, ConflictResolution
from .forms import EmployeeForm, DepartmentForm, FeedbackForm, ConflictResolutionForm


# View for listing all employees
def EmployeeListView(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})


# View for creating a new employee
def EmployeeCreateView(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_name:employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})


# View for displaying employee details
def EmployeeDetailView(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employee_detail.html', {'employee': employee})


# View for updating an existing employee
def EmployeeUpdateView(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('app_name:employee_detail', pk=pk)
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_form.html', {'form': form})


# View for deleting an employee
def EmployeeDeleteView(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('app_name:employee_list')
    return render(request, 'employee_confirm_delete.html', {'employee': employee})


# Similar CRUD views for Department, Feedback, and ConflictResolution models...
