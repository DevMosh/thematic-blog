from django.db import models


class CommentAbs(models.Model):
    class Meta:
        abstract = True

    comment = models.TextField(
        max_length=1000,
        blank=True, null=False,
    )
    count_like = models.PositiveIntegerField(default=0)
