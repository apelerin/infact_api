# flake8: noqa: E501
import scrapy
from scrapy import Spider
from api.models import Journal, Article
from mag_web.scraper.items import ScraperItemArticle


# TODO: Factorize browser and article page to harmonize when multiple modules exists
from mag_web.scraper.spiders.tools import match_category


class MarianneBrowser(Spider):
    name = "leparisien"
    start_urls = ["https://www.leparisien.fr/"]
    journal = Journal.objects.get(name="Le Parisien")

    def parse(self, response, **kwargs):
        articles_link = response.xpath('//section[@id="left"]/div[not(contains(@class, "ad_element"))]/div[not(.//span[@class="tag label abo"]) and not(contains(@class, "sub-anchor-body")) and not(contains(@class, "ad_element"))]').getall()
        for articles_link in articles_link:
            url = response.urljoin(articles_link)
            yield scrapy.Request(url=url, callback=self.parse_article)

    def parse_article(self, response):
        """ Scrapes the article page and returns a ScraperItemArticle object """
        item = ScraperItemArticle()
        title = None
        item['title'] = title

        # Basic handling of pre-existing articles
        # TODO : Use a better approach with multiple fields
        if Article.objects.filter(title=item['title']).exists():
            return

        item['image_link'] = None
        item['author'] = None

        item['body'] = None
        item['journal'] = None
        item['link'] = None
        item['date'] = None

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
