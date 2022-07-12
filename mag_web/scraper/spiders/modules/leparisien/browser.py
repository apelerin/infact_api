# flake8: noqa: E501
from datetime import datetime

import scrapy
from scrapy import Spider
from api.models import Journal, Article
from mag_web.scraper.items import ScraperItemArticle


# TODO: Factorize browser and article page to harmonize when multiple modules exists
from mag_web.scraper.spiders.tools import match_category


class LeParisienBrowser(Spider):
    name = "Le Parisien"
    start_urls = ["https://www.leparisien.fr/"]
    journal = Journal.objects.get(name="Le Parisien")

    def parse(self, response, **kwargs):
        articles_link = response.xpath('//section[@id="left"]/div[not(contains(@class, "ad_element"))]/div[not(.//span[@class="tag label abo"]) and not(contains(@class, "sub-anchor-body")) and not(contains(@class, "ad_element")) and not(.//div[@class="icon svg video"])]/a/@href').getall()
        for url in articles_link:
            yield scrapy.Request(url='https:' + url, callback=self.parse_article)

    def parse_article(self, response):
        """ Scrapes the article page and returns a ScraperItemArticle object """

        title = response.xpath('//h1[@class="title_xl col margin_bottom_headline"]/text()').get()
        if Article.objects.filter(link=response.request.url).exists() or "DIRECT" in title:
            return


        item = ScraperItemArticle()

        item['title'] = title

        item['image_link'] = "https://www.leparisien.fr/" + response.xpath('//div[@id="primary_left"]//img[@class="image "]/@src').get()
        item['author'] = response.xpath('//span[@class="author ui_bold"]/span/text()').get()

        item['body'] = self.get_body(response)
        item['journal'] = self.journal
        item['link'] = response.request.url
        # todo use response.xpath('//div[@class="timestamp width_full margin_top_ten ui"]/text()').getall() and check with regex
        item['date'] = datetime.now()

        # Temporary solution to save an Article in database.
        # TODO: Use pipelines to save articles in database
        item.save()

        raw_category = response.xpath('//div[@class="breadcrumb"]/a/text()').getall()[0]
        category = match_category(raw_category.strip())
        if category is not None:
            article = Article.objects.get(title=title)
            article.categories.add(category)
        # return item

    def get_body(self, response):
        raw_body = response.xpath('//section/p[@class="paragraph text_align_left"]//text()').getall()
        return ''.join(raw_body)
