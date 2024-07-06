from django.urls import include
from django.urls import path

from src.routers import article_router

urlpatterns = [
    path('article/', include(article_router.urls))
]