class MarianneArticle:
    author = ''
    title = ''
    date = ''
    body = []

    def __init__(self, url, response):
        self.response = None
        self.url = url
        self.response = response

    def crawl_on_article(self):
        title = self.response.xpath('//h1[@class="article__heading"]/text()').get()
        image_link = self.response.css('.article__header').css('.responsive-image::attr(src)').extract_first()
        author = self.response.xpath('//address[@class="article__details"]//a[@rel="author"]/span/text()').get()
        body = self.get_body()
        return {
            'title': title,
            'image_link': image_link,
            'link': self.url,
            'author': author,
            'body': body
        }

    def get_body(self):
        abstract = self.get_abstract()
        body = [abstract]
        return body

    def get_abstract(self):
        abstract = self.response.xpath('//h2[@class="article__headline article__item"]/text()').get()
        return abstract