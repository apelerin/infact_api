from django.core.management.base import BaseCommand
from django.core.management import call_command
from api.models import Journal


class Command(BaseCommand):
    help = 'Crawl the journals'

    def handle(self, *args, **kwargs):
        for (journal) in Journal.objects.all():
            call_command('crawl', "--name=" + journal.name)
        self.stdout.write("End of crawl")
