# flake8: noqa: E501
import scrapy
from scrapy import Spider
from api.models import Journal, Article
from mag_web.scraper.items import ScraperItemArticle
from datetime import datetime


# TODO: Factorize browser and article page to harmonize when multiple modules exists
class MarianneBrowser(Spider):
    name = "marianne"
    start_urls = ["https://www.marianne.net/"]
    journal = Journal.objects.get(name="Marianne")

    def parse(self, response, **kwargs):
        articles_link = response.css('.articles-hot__list').css('.thumbnail__link::attr(href)').getall()
        for articles_link in articles_link:
            url = response.urljoin(articles_link)
            yield scrapy.Request(url=url, callback=self.parse_article)

    def parse_article(self, response):
        """ Scrapes the article page and returns a ScraperItemArticle object """
        item = ScraperItemArticle()
        item['title'] = response.xpath('//h1[@class="article__heading"]/text()').get()

        # Basic handling of pre-existing articles
        # TODO : Use a better approach with multiple fields
        if Article.objects.filter(title=item['title']).exists():
            return

        item['image_link'] = response.css('.article__header').css(
            '.responsive-image::attr(src)').extract_first()
        item['author'] = response.xpath(
            '//address[@class="article__details"]//a[@rel="author"]/span/text()').get()
        # item['body'] = self.get_body(response)
        item['body'] = {'abstract': self.get_abstract(response)}
        item['journal'] = self.journal
        item['date'] = datetime.now()

        # Temporary solution to save an Article in database.
        # TODO: Use pipelines to save articles in database
        item.save()
        # return item

    def get_body(self, response):
        # TODO: Parse the entire body of the article
        abstract = self.get_abstract(response)
        body = [abstract]
        return body

    def get_abstract(self, response):
        abstract = response.xpath('//h2[@class="article__headline article__item"]/text()').get()
        return abstract
