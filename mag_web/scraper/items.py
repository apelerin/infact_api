# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem

from api.models import Article, Journal, InformationHub, Category


class ScraperItemArticle(DjangoItem):
    django_model = Article


class ScraperItemJournal(DjangoItem):
    django_model = Journal


class ScraperItemInformationHub(DjangoItem):
    django_model = InformationHub


class ScraperItemCategory(DjangoItem):
    django_model = Category
