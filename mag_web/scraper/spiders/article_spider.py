import logging

logging.basicConfig(level=logging.INFO)


class ArticlePageSpider:
    """ Handle article page information scraping logic """

    def __init__(self, article_url):
        self.article_url = article_url

    def get_article_title(self):
        """ Retrieve article title """
        logging.error("Not implemented")

    def get_article_body(self):
        """ Retrieve article body """
        logging.error("Not implemented")

    def get_article_author(self):
        """ Retrieve article author """
        logging.error("Not implemented")

    def get_article_date(self):
        """ Retrieve article date """
        logging.error("Not implemented")

    def get_article_links(self):
        """ Retrieve article links """
        logging.error("Not implemented")
