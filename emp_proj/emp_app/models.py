from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, null=False, default='Your_Default_Value')
    location = models.CharField(max_length=100, null=False, default='Location')

    def __str__(self):
        return self.name   

class Role(models.Model):
    name = models.CharField(max_length=100, null=False, default='Role Name')


    def __str__(self):
        return self.name

    

class Employee(models.Model):
    first_name = models.CharField(max_length=100, null=False, default='Your first name')
    last_name = models.CharField(max_length=100, null=False, default='Your last name')
    dept = models.ForeignKey(Department, default=1, on_delete=models.CASCADE)  # Default to a valid department ID
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Default salary to 0.00
    bonus = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Default bonus to 0.00
    role = models.ForeignKey(Role, default=1, on_delete=models.CASCADE)  # Default to a valid role ID
    phone = models.CharField(max_length=100, default='0')
    hire_date = models.DateField(default='2000-01-01')  # Default hire date to a valid date

    def __str__(self):
        return "%s %s %s" %(self.first_name, self.last_name, self.phone)

