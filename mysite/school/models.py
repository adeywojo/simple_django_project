from django.db import models


class School(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Certificate_type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Grade(models.Model):
    type = models.CharField(max_length=2)

    def __str__(self):
        return self.type


class Faculty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Student(models.Model):
    fullname = models.CharField(max_length=100)
    year_of_grad = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    grade = models.ForeignKey(Grade, on_delete=models.PROTECT)
    school = models.ForeignKey(School, on_delete=models.PROTECT)
    certificate_type = models.ForeignKey(Certificate_type, on_delete=models.PROTECT)

    def __str__(self):
        return self.fullname
