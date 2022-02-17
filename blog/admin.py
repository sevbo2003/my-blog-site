from django.contrib import admin
from .models import Author, Category, Tags, Post, Comment

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Tags)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'top', 'author', 'category', 'created_at')
    list_filter = ('language', 'top', 'category', 'created_at')
    search_fields = ('title', 'body', 'author', 'category')
    # prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created_at')
    list_filter = ('post',)
    search_fields = ('message', 'name', 'email')
