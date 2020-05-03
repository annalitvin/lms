from django.db import models

# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=40, null=False)
    specialty = models.CharField(max_length=40, null=False)
    course_start = models.DateField()


