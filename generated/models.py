from django.db import models

class Department(models.Model):
    """
    Model representing a department in the company.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    """
    Model representing an employee.
    """
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    hire_date = models.DateField()
    job_title = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subordinates')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Feedback(models.Model):
    """
    Model representing feedback for an employee.
    """
    id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    feedback_text = models.TextField()

    def __str__(self):
        return f'Feedback for {self.employee}'


class Meeting(models.Model):
    """
    Model representing a meeting.
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    participants = models.ManyToManyField(Employee)

    def __str__(self):
        return self.title