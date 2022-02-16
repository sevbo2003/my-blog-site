from django.shortcuts import render, get_object_or_404
from .models import Category, Author, Tags, Post


def index(request):
    posts = Post.objects.all()
    top_posts = Post.objects.filter(top=True)[:3]
    context = {
        'posts': posts,
        'top_posts': top_posts
    }
    return render(request, 'index.html', context)