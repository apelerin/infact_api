from django.core.management.base import BaseCommand
from api.models import Journal, Category
import logging

logging.basicConfig(level=logging.INFO)

JOURNALS = [
    {
        'name': 'Marianne',
    },
]

CATEGORIES = [
    {
        'name': 'Économie',
        'match': ['Économie', 'Entreprises', 'Finance']
    },
    {
        'name': 'Société',
        'match': ['Société', 'Justice', 'Santé', 'Logement']
    },
    {
        'name': 'Politique',
        'match': ['Politique', 'Gouvernement']
    },
    {
        'name': 'Culture',
        'match': ['Culture', 'Cinéma', 'Télévision', 'Littérature']
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
        initialize_categories()
    elif mode == 'fill':
        fill_journals()
        fill_categories()


def initialize_journals():
    for journal in JOURNALS:
        Journal.objects.create(**journal)
    logging.info('Journals initialized')


def initialize_categories():
    for category in CATEGORIES:
        Category.objects.create(**category)
    logging.info('Categories initialized')


def fill_categories():
    for category in CATEGORIES:
        try:
            Category.objects.get(name=category['name'])
        except Category.DoesNotExist:
            Category.objects.create(**category)
            logging.info('Category {} added'.format(category['name']))
        else:
            pass


def fill_journals():
    for journal in JOURNALS:
        try:
            Journal.objects.get(name=journal['name'])
        except Journal.DoesNotExist:
            Journal.objects.create(**journal)
            logging.info('Journals {} added'.format(journal['name']))
        else:
            pass
