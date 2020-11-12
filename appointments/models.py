from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Appt(models.Model):
    tutor_num = models.IntField()
    student_num = models.IntField()
    sched_time = models.DateTimeField()
    meeting_link = models.URLField()
