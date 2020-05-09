import datetime


from django.db import models

# Create your models here.
from faker import Faker


class Teacher(models.Model):
    first_name = models.CharField(max_length=40, null=False)
    last_name = models.CharField(max_length=20, null=False)
    phone_number = models.CharField(max_length=14, null=False)
    email = models.EmailField()
    user_name = models.CharField(max_length=100)
    employment_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.phone_number}'

    @classmethod
    def generate_teacher(cls):
        faker = Faker(['it_IT', 'en_US', 'uk_UA'])

        teacher = cls(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            phone_number=faker.phone_number(),
            email=faker.email(),
            user_name=faker.user_name()
        )
        teacher.save()
