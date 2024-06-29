from django.db import models

from backend.general_layout.models.abs_artilce import ArticleAbs


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
        on_delete=models.SET_NULL
    )

