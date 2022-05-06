from api.models import Article, InformationHub, Category, Journal
from rest_framework import viewsets
from api.serializers import ArticleSerializer, CategorySerializer, InformationHubSerializer, JournalSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows articles to be viewed or edited.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_queryset(self):
        author = self.request.query_params.get('author', None)
        if author is not None:
            queryset = Article.objects.filter(author=author)
        else:
            queryset = Article.objects.all()
        return queryset


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class InformationHubViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = InformationHub.objects.all()
    serializer_class = InformationHubSerializer


class JournalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
