from django.core.management import BaseCommand, CommandError
from group.models import Group


class Command(BaseCommand):
    help = "Added new groups in database"

    def add_arguments(self, parser):
        parser.add_argument("number_group", type=int,
                            help="Number of groups to add to the database")

    def handle(self, *args, **options):
        number_groups = options['number_group']

        try:
            for _ in range(number_groups):
                Group.generate_group()
        except Exception as ex:
            raise CommandError(f'Data added fail! {ex}')
        self.stdout.write(self.style.SUCCESS(f'Data added successfully! {number_groups}'))
