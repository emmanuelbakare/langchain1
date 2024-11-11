from django.db import models


class Department(models.Model):
    # Primary key for Department with unique name and manager reference
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    manager = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    # Primary key for Employee with personal details and department reference
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    hire_date = models.DateField()
    position = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Feedback(models.Model):
    # Primary key for Feedback with employee reference and created_by reference
    id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    feedback_date = models.DateField()
    comments = models.TextField()
    created_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Feedback for {self.employee}'


class ConflictResolution(models.Model):
    # Primary key for ConflictResolution with employee reference and resolved_by reference
    id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    resolution_date = models.DateField()
    description = models.TextField()
    resolved_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Resolution for {self.employee}'
