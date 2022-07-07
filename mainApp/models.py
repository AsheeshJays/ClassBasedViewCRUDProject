from django.db import models

class Employee(models.Model):
    empID = models.CharField(max_length=15)
    empName = models.CharField(max_length=50)
    empDesgination = models.CharField(max_length=50)
    empSalary = models.IntegerField()

