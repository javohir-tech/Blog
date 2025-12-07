from django.contrib import admin
from .models import Article, Comment

class CommentLayn(admin.TabularInline):
    model = Comment
    extra = 0

class ArticleKorisnih(admin.ModelAdmin):
    inlines = [CommentLayn]

admin.site.register(Article, ArticleKorisnih)
admin.site.register(Comment)
