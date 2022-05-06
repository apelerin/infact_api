from datetime import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from rest_framework.test import RequestsClient

from api.models import Journal, Article
from api.views import JournalViewSet, ArticleViewSet


class ApiTest(APITestCase):
    def setUp(self) -> None:
        self.factory = APIRequestFactory()

    def test_create_journal(self):
        """ Test API endpoint for creating journal """
        request = self.factory.post(reverse('journal-list'), {
            'name': 'Test journal',
        })
        view_set = JournalViewSet.as_view({'post': 'create'})
        response = view_set(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_articles(self):
        """ Test API endpoint for getting list of articles """
        pass

    def test_get_article(self):
        """ Test API endpoint for getting single article """
        pass

    def test_get_categories(self):
        """ Test API endpoint for getting list of categories """
        pass

    def test_get_category(self):
        """ Test API endpoint for getting single category """
        pass

    """
    def test_get_article(self):
        Journal.objects.create(name='Test journal')
        Article.objects.create(journal=Journal.objects.get(name='Test journal'), title='Test article',
                               body={'text': 'Test text'},
                               date=datetime.now(), author='Axel')
        request = self.factory.get('/articles/?author=Axel')
        print(request)
        view_set = ArticleViewSet.as_view({'get': 'retrieve'})
        response = view_set(request)
        print(response)
        assert response.data, {
            'title': 'Test article',
            'author': 'Axel',
            'journal': Journal.objects.get(name='Test journal'),
            'body': {
                'text': 'Test text'
            },
        }
    """