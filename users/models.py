from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_addr = models.EmailField()

    meeting_link = models.URLField()
    courses = models.TextField()
    password = models.CharField(max_length=50)
    university = models.CharField(max_length=100)
