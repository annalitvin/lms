import datetime

from django.db import models

# Create your models here.
from faker import Faker

from group.models import Group


class Student(models.Model):
    first_name = models.CharField(max_length=40, null=False)
    last_name = models.CharField(max_length=20, null=False)
    email = models.EmailField(max_length=50, null=False)
    birthdate = models.DateField(default=datetime.date.today)
    phone_number = models.CharField(max_length=14, null=True)
    group = models.ForeignKey(to=Group, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.birthdate}'

    @classmethod
    def generate_student(cls):
        faker = Faker()

        student = cls(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            phone_number=faker.phone_number(),
        )
        student.save()
