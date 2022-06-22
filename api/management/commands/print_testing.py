from django.core.management import BaseCommand
from django.core.management import call_command

from api.management.commands.seed import clear_data


class Command(BaseCommand):
    help = "Print for testing purpose"

    def handle(self, *args, **options):
        self.stdout.write("Test scheduler")
