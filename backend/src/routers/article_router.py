from rest_framework import routers

from view.article_view import ArticleView

article_router = routers.SimpleRouter()
article_router.register(r'', ArticleView)