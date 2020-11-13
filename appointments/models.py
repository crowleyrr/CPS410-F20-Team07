from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Appt(models.Model):
    """
    The Appt model creates objects representing existing appointments.  It
    holds info pertaining to who the tutor is (referencing the tutor's primary key),
    who the student is (referencing the student's primary key), the scheduled
    date and time of the meeting, and the meeting link.  The meeting link
    is a foreign key referencing the tutor's meeting space URL.
    """
    tutor_num = models.IntegerField()
    student_num = models.IntegerField()
    sched_time = models.DateTimeField()
    meeting_link = models.URLField()
