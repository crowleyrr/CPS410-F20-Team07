from django.contrib import admin
# from django.contrib.contenttypes.admin import GenericTabularInline
#
# from users.models import Student
# # Register your models here.
# class StudentInline(GenericTabularInline):
#     model = Student
from .models import Student

admin.site.register(Student)
