from scrapy import Spider


# from mag_web.scraper.spiders.browser_spider import BrowserSpider


class MarianneBrowser(Spider):
    name = "marianne"
    start_urls = ["https://www.marianne.net/"]

    def parse(self, response, **kwargs):
        articles_link = response.css('.articles-hot__list').css('.thumbnail__link::attr(href)').getall()
        print(articles_link)
