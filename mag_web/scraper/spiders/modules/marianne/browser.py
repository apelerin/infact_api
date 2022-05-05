import scrapy
from scrapy import Spider
from  api.models import Journal, Article
from .article import MarianneArticle

class MarianneBrowser(Spider):
    name = "marianne"
    start_urls = ["https://www.marianne.net/"]
    journal = Journal.objects.get(name="Marianne")

    def parse(self, response, **kwargs):
        articles_link = response.css('.articles-hot__list').css('.thumbnail__link::attr(href)').getall()
        for articles_link in articles_link:
            article_handler = MarianneArticle(response.urljoin(articles_link), response)
            url = response.urljoin(articles_link)
            try:
                article = scrapy.Request(url=url, callback=article_handler.crawl_on_article())
            except Exception as e:
                print(e)
                pass
            else:
                # TODO: Replace direct insert with a scrapy pipeline
                # Temporary solution until we have a pipeline
                Article(article).save() # Save article in database
                yield article
