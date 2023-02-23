from django.db import models

class Employees(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    age = models.PositiveSmallIntegerField()
    date_of_birth = models.DateField(auto_now_add=True)