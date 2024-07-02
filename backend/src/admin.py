
from django.contrib import admin

from src.models import Article, Comment, CommentLike, Category, ArticleFavorites

admin.site.register(
    [
        Category,
        Article,
        ArticleFavorites,
        Comment,
        CommentLike,
    ]
)

# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('')
