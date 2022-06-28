from django.core.management.base import BaseCommand
from api.models import Article, Journal, InformationHub, Category
from django.utils import timezone
import logging

logging.basicConfig(level=logging.INFO)

# python manage.py seed --mode=refresh

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'


class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(options['mode'])
        self.stdout.write('done.')


def run_seed(mode):
    """ Seed database based on mode

    :param mode: refresh / clear
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    # Create data
    create_categories()
    create_journals()
    create_articles()
    create_information_hubs()


def clear_data():
    """Deletes all the table data"""
    logging.info('Clearing data...')
    Article.objects.all().delete()
    InformationHub.objects.all().delete()
    Category.objects.all().delete()
    Journal.objects.all().delete()


def create_categories():
    """ Create categories """
    categories = [
        {
            'name': 'Actualité',
        },
        {
            'name': 'Science',
        },
        {
            'name': 'Economie',
        }
    ]
    for category in categories:
        Category.objects.create(**category)
    logging.info('Categories created.')


def create_journals():
    """ Create journals """

    journals = [
        {
            'name': 'Le Monde',
        },
        {
            'name': 'Le Figaro',
        },
        {
            'name': 'Le Parisien',
        },
    ]
    for journal in journals:
        Journal.objects.create(**journal)
    logging.info('Journals created.')


def create_articles():
    """ Create articles """

    articles = [
        {
            'author': 'Jean-Michel',
            'title': 'La reproduction de la nature',
            'date': timezone.now(),
            'body': {
                'p1': '<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>'
            },
            'link': 'https://www.lefigaro.fr/culture/patrimoine/l-egypte-restaure-la-plus-ancienne-synagogue-du-moyen-orient-20220501',
            'image_link': 'https://i.f1g.fr/media/cms/704x396_cropupscale/2022/04/29/90579152af081b99d6ed26a5a9f0ed305ae4f93afb244d16614c6003cfe88276.jpg',
            'journal': Journal.objects.get(name='Le Figaro'),
        },
        {
            'author': 'Baptiste',
            'title': 'Les tortues en bourse',
            'date': timezone.now(),
            'body': {
                '<p1>': '<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>'
            },
            'link': 'https://www.lefigaro.fr/culture/patrimoine/l-egypte-restaure-la-plus-ancienne-synagogue-du-moyen-orient-20220501',
            'image_link': 'https://i.f1g.fr/media/cms/704x396_cropupscale/2022/04/29/90579152af081b99d6ed26a5a9f0ed305ae4f93afb244d16614c6003cfe88276.jpg',
            'journal': Journal.objects.get(name='Le Figaro'),
        },
    ]

    categories = Category.objects.all()

    for index, article in enumerate(articles):
        instance = Article.objects.create(**article)
        instance.categories.add(categories[index])
    logging.info('Articles created.')


def create_information_hubs():
    """ Create information hub """

    informationhub = [
        {
            'title': 'La reproduction de la nature',
            'original_source_link': 'https://www.lefigaro.fr/culture/patrimoine/a-tallinn-un-navire-du-xiiie-siecle-etonnamment-bien-conserve-surgit-de-terre-20220501',
        },
        {
            'title': 'Les choses',
            'original_source_link': 'https://www.lefigaro.fr/culture/patrimoine/a-tallinn-un-navire-du-xiiie-siecle-etonnamment-bien-conserve-surgit-de-terre-20220501',
        },
    ]

    articles = Article.objects.all()
    articles_list = [
        articles[0],
        *[articles[1], articles[0]],
    ]

    for index, informationhub in enumerate(informationhub):
        instance = InformationHub.objects.create(**informationhub)
        instance.articles.add(articles_list[index])
    logging.info('InformationHub created.')
