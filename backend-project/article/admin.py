from django.contrib import admin
from django.contrib.admin import StackedInline
from .models import Article , Comment
# Register your models here.

class CommentInline(admin.StackedInline):
    '''Stacked Inline View for Comment'''
    model = Comment
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    inlines=[CommentInline]

admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment)