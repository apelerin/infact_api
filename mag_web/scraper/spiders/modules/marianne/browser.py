import scrapy
from scrapy import Spider


# from mag_web.scraper.spiders.browser_spider import BrowserSpider


class MarianneBrowser(Spider):
    name = "marianne"
    start_urls = ["https://www.marianne.net/"]

    # response = None
    # todo separate article from browser

    def parse(self, response, **kwargs):
        # self.response = response
        articles_link = response.css('.articles-hot__list').css('.thumbnail__link::attr(href)').getall()
        for articles_link in articles_link:
            url = response.urljoin(articles_link)
            yield scrapy.Request(url=url, callback=self.parse_article)

    def parse_article(self, response):
        # self.response = response
        title = response.xpath('//h1[@class="article__heading"]/text()').get()
        img_link = response.css('.article__header').css('.responsive-image::attr(src)').extract_first()
        author = response.xpath('//address[@class="article__details"]//a[@rel="author"]/span/text()').get()

    def get_body(self, response):
        body = []
        return body

    def get_abstract(self, response):
        abstract = response.xpath('//h2[@class="article__headline article__item"]/text()').get()
        return abstract
