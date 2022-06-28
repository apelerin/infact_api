from rest_framework import serializers

from api.models import Journal, Category, Article, InformationHub


class JournalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Journal
        fields = ['name']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ['author', 'title', 'date', 'body', 'link',
                  'image_link', 'journal', 'journal', 'categories']


class InformationHubSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InformationHub
        fields = ['title', 'original_source_link', 'articles']
