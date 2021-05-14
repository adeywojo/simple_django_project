from django.contrib import admin
from .models import School, Student, Grade, Certificate_type, Faculty, Department

admin.site.register(School)
admin.site.register(Student)
admin.site.register(Grade)
admin.site.register(Certificate_type)
admin.site.register(Faculty)
admin.site.register(Department)
