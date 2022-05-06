from django.core.management import BaseCommand

from api.models import Article, InformationHub


class Command(BaseCommand):
    help = 'Create hub_information from articles in the database'

    def handle(self, *args, **options):
        self.stdout.write("Creating hubs...")
        self.create_hubs()
        self.stdout.write("Done.")

    def create_hubs(self):
        articles = Article.objects.all()

        for _ in range(3):
            sample_articles = articles.order_by('?')[:3]
            instance = InformationHub.objects.create(
                title=sample_articles[0].title,
                original_source_link="https://www.cdiscount.com/pdt2/2/6/9/1/1200x1200/auc2009706636269/rw/244677-18cm-rainbow-cute-alpacasso-kawaii-alpaca-l.jpg"
            )
            instance.articles.add(*sample_articles)
