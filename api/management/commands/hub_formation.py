import random

from django.core.management import BaseCommand

from api.models import Article, InformationHub


class Command(BaseCommand):
    help = 'Create hub_information from articles in the database'
    images_url = [
        "https://www.thespruce.com/thmb/t13CIs9CH0HfuggdQ-DU9zk_QHo=/3780x2126/smart/filters:no_upscale()/do-ducks-have-teeth-4153828-hero-9614a7e9f4a049b48e8a35a9296c562c.jpg",
        "https://www.cdiscount.com/pdt2/2/6/9/1/1200x1200/auc2009706636269/rw/244677-18cm-rainbow-cute-alpacasso-kawaii-alpaca-l.jpg",
        "https://maxitacos.fr/wp-content/uploads/2019/09/coca-cherry-boite-1.png",
        "https://www.jardiner-malin.fr/wp-content/uploads/2021/12/Cactophile-cactus-succulente.jpg"
    ]

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
                original_source_link=self.images_url[random.randint(0, self.images_url.__len__() - 1)],
            )
            instance.articles.add(*sample_articles)
