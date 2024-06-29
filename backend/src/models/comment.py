from django.db import models

from backend.config import settings
from backend.general_layout.models.abs_comment import CommentAbs


class Comment(CommentAbs):
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )


class CommentLike(models.Model):
    class Meta:
        verbose_name = "Лайк на комментарий"
        verbose_name_plural = "Лайки на комментарии"

    comment = models.ForeignKey(
        Comment,
        related_name="com_like",
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL
    )


