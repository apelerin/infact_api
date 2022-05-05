import scrapy
from scrapy import Spider


# from mag_web.scraper.spiders.browser_spider import BrowserSpider
from .article import MarianneArticle


class MarianneBrowser(Spider):
    name = "marianne"
    start_urls = ["https://www.marianne.net/"]

    # todo separate article from browser

    def parse(self, response, **kwargs):
        # self.response = response
        articles_link = response.css('.articles-hot__list').css('.thumbnail__link::attr(href)').getall()
        for articles_link in articles_link:
            article_handler = MarianneArticle(response.urljoin(articles_link), response)
            url = response.urljoin(articles_link)
            yield scrapy.Request(url=url, callback=article_handler.crawl_on_article())
