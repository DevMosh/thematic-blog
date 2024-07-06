from django.contrib import admin

from src.models import Article, Comment, CommentLike, Category, ArticleFavorites

admin.site.register(
    [
        Category,
        ArticleFavorites,
        Comment,
        CommentLike,
    ]
)


@admin.register(Article)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'text_content', 'image', 'category', )
    exclude = ("count_like",)
