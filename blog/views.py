from django.shortcuts import render, get_object_or_404
from .models import Category, Author, Tags, Post
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    key = request.GET.get('search')
    if key:
        posts = Post.objects.filter(Q(title__icontains=key) | Q(category__category__icontains=key))
    else:
        posts = Post.objects.all()
    page_num = request.GET.get('page', 1)
    paginator = Paginator(posts, 4)
    try:
        posts = paginator.page(page_num)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    top_posts = Post.objects.filter(top=True)[:3]
    context = {
        'posts': posts,
        'top_posts': top_posts,
    }
    return render(request, 'index.html', context)


def uz_lang_posts(request):
    key = request.GET.get('search')
    if key:
        posts = Post.objects.filter(Q(title__icontains=key) | Q(category__category__icontains=key)).filter(language__exact='uz')
    else:
        posts = Post.objects.filter(language__exact='uz')
    page_num = request.GET.get('page', 1)
    paginator = Paginator(posts, 4)
    try:
        posts = paginator.page(page_num)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    top_posts = Post.objects.filter(top=True)[:3]
    context = {
        'posts': posts,
        'top_posts': top_posts,
    }
    return render(request, 'uzb_lang_posts.html', context)


def cat_posts(request, id, category):
    cat = get_object_or_404(Category, id=id, category=category)
    posts = Post.objects.filter(category=cat)
    page_num = request.GET.get('page', 1)
    paginator = Paginator(posts, 4)
    try:
        posts = paginator.page(page_num)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'cat': cat,
        'posts': posts
    }
    return render(request, 'category.html', context)
