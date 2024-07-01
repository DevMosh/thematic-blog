from django.db import models

from config import settings
from general_layout.models.abs_artilce import ArticleAbs


class Category(models.Model):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    name = models.CharField(max_length=256, null=False)


class Article(ArticleAbs):
    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
    )


class ArticleFavorites(models.Model):
    class Meta:
        verbose_name = "Избранная статья"
        verbose_name_plural = "Избранные статьи"

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        verbose_name="Статья"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )
