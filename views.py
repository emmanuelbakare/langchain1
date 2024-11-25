from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Contact, Address, Employee
from .forms import UserForm, ContactForm, AddressForm, EmployeeForm

# User CRUD Views

def user_list(request):
    users = User.objects.all()  # Fetch all users
    return render(request, 'user_list.html', {'users': users})


def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            return redirect('user_list')
    else:
        form = UserForm()  # Display empty form
    return render(request, 'user_form.html', {'form': form})


def user_update(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()  # Save the updated user
            return redirect('user_list')
    else:
        form = UserForm(instance=user)  # Display form with existing user data
    return render(request, 'user_form.html', {'form': form})


def user_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()  # Delete the user
        return redirect('user_list')
    return render(request, 'user_confirm_delete.html', {'user': user})


# Contact CRUD Views

def contact_list(request):
    contacts = Contact.objects.all()  # Fetch all contacts
    return render(request, 'contact_list.html', {'contacts': contacts})


def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new contact
            return redirect('contact_list')
    else:
        form = ContactForm()  # Display empty form
    return render(request, 'contact_form.html', {'form': form})


def contact_update(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()  # Save the updated contact
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)  # Display form with existing contact data
    return render(request, 'contact_form.html', {'form': form})


def contact_delete(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == 'POST':
        contact.delete()  # Delete the contact
        return redirect('contact_list')
    return render(request, 'contact_confirm_delete.html', {'contact': contact})


# Address CRUD Views

def address_list(request):
    addresses = Address.objects.all()  # Fetch all addresses
    return render(request, 'address_list.html', {'addresses': addresses})


def address_create(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new address
            return redirect('address_list')
    else:
        form = AddressForm()  # Display empty form
    return render(request, 'address_form.html', {'form': form})


def address_update(request, address_id):
    address = get_object_or_404(Address, id=address_id)
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()  # Save the updated address
            return redirect('address_list')
    else:
        form = AddressForm(instance=address)  # Display form with existing address data
    return render(request, 'address_form.html', {'form': form})


def address_delete(request, address_id):
    address = get_object_or_404(Address, id=address_id)
    if request.method == 'POST':
        address.delete()  # Delete the address
        return redirect('address_list')
    return render(request, 'address_confirm_delete.html', {'address': address})


# Employee CRUD Views

def employee_list(request):
    employees = Employee.objects.all()  # Fetch all employees
    return render(request, 'employee_list.html', {'employees': employees})


def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new employee
            return redirect('employee_list')
    else:
        form = EmployeeForm()  # Display empty form
    return render(request, 'employee_form.html', {'form': form})


def employee_update(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()  # Save the updated employee
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)  # Display form with existing employee data
    return render(request, 'employee_form.html', {'form': form})


def employee_delete(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        employee.delete()  # Delete the employee
        return redirect('employee_list')
    return render(request, 'employee_confirm_delete.html', {'employee': employee})