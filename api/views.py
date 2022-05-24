from api.models import Article, InformationHub, Category, Journal
from rest_framework import viewsets
from api.serializers import ArticleSerializer, CategorySerializer, InformationHubSerializer, JournalSerializer


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows articles to be viewed or edited.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_queryset(self):
        # Filter by author
        author = self.request.query_params.get('author', None)
        if author is not None:
            queryset = Article.objects.filter(author=author)
        else:
            queryset = Article.objects.all()
        return queryset


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class InformationHubViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows information hubs to be viewed or edited.
    """
    queryset = InformationHub.objects.all()
    serializer_class = InformationHubSerializer


class JournalViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows journals to be viewed or edited.
    """
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
