from django.db import models

from config import settings
from general_layout.models.abs_comment import CommentAbs, CommentReplyAbs


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
        null=True,
        on_delete=models.SET_NULL
    )


class CommentReply(CommentReplyAbs):
    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"

    comment = models.ForeignKey(
        Comment,
        related_name="комментарий",
        on_delete=models.CASCADE,
        null=False
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )
