from django.core.management import BaseCommand, CommandError

from teacher.models import Teacher


class Command(BaseCommand):
    help = "Added new teachers in database"

    def add_arguments(self, parser):
        parser.add_argument("number_teacher", type=int,
                            help="Number of teachers to add to the database")

    def handle(self, *args, **options):
        number_teachers = options['number_teacher']

        try:
            for _ in range(number_teachers):
                Teacher.generate_teacher()
        except Exception as ex:
            raise CommandError(f'Data added fail! {ex}')
        self.stdout.write(self.style.SUCCESS(f'Data added successfully! {number_teachers}'))
