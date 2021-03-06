import datetime
import random
import string

from django.db import models

# Create your models here.
from teacher.models import Teacher


class Classroom(models.Model):
    name = models.CharField(max_length=64)
    floor = models.SmallIntegerField(null=True)

    def __str__(self):
        return f'{self.name} - Floor# {self.floor}'

    @classmethod
    def generate_classroom(cls):

        classroom = cls(
            name=f'Classroom-{random.choice(range(5))}',
            floor=random.choice(range(5))
        )
        classroom.save()


class Group(models.Model):

    ONLINE = 'online'
    OFFLINE = 'offline'
    TYPE_CHOICES = [
        (ONLINE, 'online'),
        (OFFLINE, 'offline')
    ]

    name = models.CharField(max_length=40, null=False, blank=False, unique=True)
    specialty = models.CharField(max_length=40, null=False, blank=False)
    course_name = models.CharField(max_length=80, null=False, blank=False)
    number_persons = models.PositiveSmallIntegerField()
    type = models.CharField(max_length=8, null=False, blank=False, choices=TYPE_CHOICES)
    is_paid = models.BooleanField(null=False, blank=False)
    date_start = models.DateField(default=datetime.date.today)
    teacher = models.ForeignKey(to=Teacher, null=True, on_delete=models.SET_NULL)
    classroom = models.ManyToManyField(to=Classroom, related_name='group')

    def __str__(self):
        return f'{self.name}, {self.specialty}, ' \
            f'{self.course_name}, ' \
            f'{self.number_persons}, ' \
            f'{self.type}, {self.date_start}'

    @classmethod
    def generate_group(cls, teachers=None):

        if teachers is None:
            teachers = list(Teacher.objects.all())

        courses_name = None

        specialty = random.choice(["Python", "SQL", "PHP"])

        if specialty == 'Python':
            courses_name = ["Introduction Python", "Python", "Machine Learning and Deep Learning", "Django"]
        elif specialty == 'SQL':
            courses_name = ["Introduction SQL", "SQL"]
        elif specialty == 'PHP':
            courses_name = ["Introduction PHP", "PHP", "Symphony"]

        course_name = random.choice(courses_name)

        year = random.randrange(2014, 2019)
        month = random.randrange(1, 11)
        day = random.randrange(1, 28)

        generation_symbols = ''.join([random.choice(string.ascii_lowercase+string.digits) for _ in range(25)])

        group = cls(
            name=f'group-{generation_symbols}',
            specialty=specialty,
            course_name=course_name,
            number_persons=random.randrange(1, 15),
            type=random.choice(["online", "offline"]),
            is_paid=random.choice([True, False]),
            date_start=datetime.datetime(year, month, day),
            teacher=random.choice(teachers)
        )
        group.save()
