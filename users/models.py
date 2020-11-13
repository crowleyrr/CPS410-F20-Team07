from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
    """
    A Student object represents a user who is a student.  The model holds the
    student's first and last name, email address, courses, password, and their
    affiliated university.
    """
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_addr = models.EmailField()
    courses = models.TextField()
    password = models.CharField(max_length=50)
    university = models.CharField(max_length=100)

class Tutor(models.Model):
    """
    A Tutor object represents a user who is a tutor. The model holds the tutor's
    first and last name, email address, courses, password, their affiliated
    university, and a link to their meeting space which is a valid URL.
    """
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_addr = models.EmailField()

    meeting_link = models.URLField()
    courses = models.TextField()
    password = models.CharField(max_length=50)
    university = models.CharField(max_length=100)
