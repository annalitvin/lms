from django.core.management import BaseCommand, CommandError

from group.models import Group
from student.models import Student


class Command(BaseCommand):
    help = "Added new students in database"

    def add_arguments(self, parser):
        parser.add_argument("number_student", type=int,
                            help="Number of students to add to the database")

    def handle(self, *args, **options):
        number_students = options['number_student']

        try:
            Student.objects.all().delete()
            groups = list(Group.objects.all())
            for _ in range(number_students):
                Student.generate_student(groups)
        except Exception as ex:
            raise CommandError(f'Data added fail! {ex}')
        self.stdout.write(self.style.SUCCESS(f'Data added successfully! {number_students}'))
