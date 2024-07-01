

from rest_framework import viewsets

from backend.src.models.article import Article


class ArticleView(viewsets.ViewSet):
    """ Тут """
    http_method_names = ['get', 'post', 'path']

    def list(self, request):
        articles = Article.objects.all()

