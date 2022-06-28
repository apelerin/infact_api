from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Print for testing purpose"

    def handle(self, *args, **options):
        self.stdout.write("Test scheduler")
