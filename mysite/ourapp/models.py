from django.db import models
from datetime import datetime


class School(models.Model):
    name = models.CharField(max_length=400)
    address = models.CharField(max_length=400)
    zip_code = models.IntegerField()


class Student(models.Model):
    School = models.ForeignKey(School, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    department = models.CharField(max_length=50)
    date_of_resumption = models.DateField(default=datetime.today)
