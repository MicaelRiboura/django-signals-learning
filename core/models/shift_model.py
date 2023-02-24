from django.db import models
from core.models.employee_model import Employees
from datetime import datetime

class Shifts(models.Model):
    employees_shift = models.ManyToManyField(Employees, through='ShiftsEmployees', related_name='shifts')
    wage_bonus = models.DecimalField(max_digits=4, decimal_places=2, default=50.00)
    total_hours = models.IntegerField(default=8)
    shift_date = models.DateField(default=datetime.now())


class ShiftsEmployees(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE, null=True)
    shift = models.ForeignKey(Shifts, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('employee', 'shift')