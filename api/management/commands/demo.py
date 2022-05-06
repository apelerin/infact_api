from django.core.management import BaseCommand
from django.core.management import call_command

from api.management.commands.seed import clear_data


class Command(BaseCommand):
    help = "Generate demo data"

    def handle(self, *args, **options):
        self.stdout.write("Generate demo data...")
        clear_data()
        call_command('initialize_journals', '--mode=fill')
        call_command('crawl', '--name=marianne')
        call_command('hub_formation')
        self.stdout.write("DEMO DATA GENERATED")
