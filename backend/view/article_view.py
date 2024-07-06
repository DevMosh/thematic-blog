from django.shortcuts import get_object_or_404
from rest_framework import viewsets, serializers
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.response import Response

from src.models import Article
from src.serializers.article_serializer import ArticleSerializer


class ArticleView(viewsets.ViewSet):
    """ Просмотр, добавление и изменение статей"""

    queryset = Article.objects.all()
    http_method_names = ['get', 'post', 'path', 'delete']
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    serializer_class = ArticleSerializer

    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        article = get_object_or_404(Article, pk=pk)

    # def create(self, request):
    #     article = Article()
