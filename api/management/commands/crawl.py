from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from mag_web.scraper.spiders.modules.marianne.browser import MarianneBrowser

dict_browser = { 'marianne': MarianneBrowser }

class Command(BaseCommand):
    help = "Release the spiders"

    def add_arguments(self, parser):
        parser.add_argument('--name', type=str, help="Name of the spider")

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())

        process.crawl(dict_browser[options['name']])
        process.start()