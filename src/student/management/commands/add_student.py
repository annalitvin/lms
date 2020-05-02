from django.core.management import BaseCommand, CommandError

from student.models import Student


class Command(BaseCommand):
    help = "Added new students in database"

    def add_arguments(self, parser):
        parser.add_argument("number_student", type=int,
                            help="Number of students to add to the database")

    def handle(self, *args, **options):
        number_students = options['number_student']

        try:
            for _ in range(number_students):
                Student.generate_student()
        except Exception as ex:
            raise CommandError(f'Data added fail! {ex}')
        self.stdout.write(self.style.SUCCESS(f'Data added successfully! {number_students}'))
