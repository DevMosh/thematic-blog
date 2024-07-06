from django.db import models


class ArticleAbs(models.Model):
    class Meta:
        abstract = True

    image = models.ImageField(
        verbose_name="Обложка статьи",
        upload_to='article/%Y/%m/%d'
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Название статьи",
        null=False
    )
    date_published = models.DateTimeField(
        verbose_name="Дата публикации",
        auto_now_add=True,
        blank=False, null=False
    )
    text_content = models.TextField(
        verbose_name="Контент",
        null=False
    )
    count_like = models.IntegerField(
        default=0,
        null=False, blank=True
    )

