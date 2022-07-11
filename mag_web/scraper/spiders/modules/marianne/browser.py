# flake8: noqa: E501
import scrapy
from scrapy import Spider
from api.models import Journal, Article
from mag_web.scraper.items import ScraperItemArticle
from datetime import datetime


# TODO: Factorize browser and article page to harmonize when multiple modules exists
from mag_web.scraper.spiders.tools import match_category


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
        title = response.xpath('//h1[@class="article__heading"]/text()').get()
        item['title'] = title

        # Basic handling of pre-existing articles
        # TODO : Use a better approach with multiple fields
        if Article.objects.filter(title=item['title']).exists():
            return

        item['image_link'] = response.css('.article__header').css(
            '.responsive-image::attr(src)').extract_first()
        item['author'] = response.xpath('//address[@class="article__details"]//span/text()').get()

        item['body'] = self.get_body(response)
        item['journal'] = self.journal
        item['link'] = response.request.url
        item['date'] = response.xpath('//time/@datetime').get()

        # Temporary solution to save an Article in database.
        # TODO: Use pipelines to save articles in database
        item.save()

        raw_category = response.xpath(
            '//div[@class="breadcrumb article__item"]/span[@class="breadcrumb__item"]/span[@class="breadcrumb__item"]/a[@class="breadcrumb__label breadcrumb__label--link"]/text()').get()
        category = match_category(raw_category.strip())
        if category is not None:
            article = Article.objects.get(title=title)
            article.categories.add(category)
        # return item

    def get_body(self, response):
        # TODO: Parse the entire body of the article
        body = [response.xpath('//h2[@class="article__headline article__item"]/text()').get()]

        raw_body = response.xpath('//article/div/div[@class="article-body js-article-body"]/child::node()[not(self::strong)]//text()')
        for raw_paragraph in raw_body:
            paragraph = raw_paragraph.get()
            if paragraph:
                body.append(paragraph)
        return ''.join(body)
