import logging
logging.basicConfig(level=logging.INFO)

class Browser:
    """ Handles all browser actions for the scraper,
     such as navigating on the website, to a page
     and searching articles."""
    def __init__(self, url = None):
        self.url = url

    def go_to_website(self):
        """ Navigate to the website """
        logging.error("Not implemented")


    def go_to_article(self):
        """ Navigate to the article """
        logging.error("Not implemented")


    def search_article_by_date(self):
        """ Search for articles by date """
        logging.error("Not implemented")


    def search_recent_articles(self):
        """ Search for recent articles """
        logging.error("Not implemented")


    def search_articles_by_keyword(self):
        """ Search for articles by keyword """
        logging.error("Not implemented")


    def is_article_premium(self):
        """ Check if the article is premium gated """
        logging.error("Not implemented")
