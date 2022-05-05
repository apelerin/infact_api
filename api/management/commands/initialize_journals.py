from django.core.management.base import BaseCommand
from api.models import Article, Journal, InformationHub, Category
from django.utils import timezone
import logging
logging.basicConfig(level=logging.INFO)

JOURNALS = [
    {
        'name': 'Marianne',
    },
]

class Command(BaseCommand):
    help = "Initialize the database with journals or add the ones that are missing"

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('Initializing journals...')
        run_initialize(options['mode'])
        self.stdout.write('done.')


def run_initialize(mode):
    """ Initialize the database with journals or add the ones that are missing based on the mode
    :param mode: initialize/fill
    :return:
    """
    if mode == 'initialize':
        initialize_journals()
    elif mode == 'fill':
        fill_journals()

def initialize_journals():
    for journal in JOURNALS:
        Journal.objects.create(**journal)
    logging.info('Journals initialized')

def fill_journals():
    for journal in JOURNALS:
        try:
            Journal.objects.get(name=journal['name'])
        except Journal.DoesNotExist:
            Journal.objects.create(**journal)
            logging.info('Journals {} added'.format(journal['name']))
        else:
            pass
